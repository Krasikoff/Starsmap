from rest_framework import serializers

from employee.models import (
    Competence, LastRating, Position, Rating, Skill, Team, User, Candidate,
    Vacancy,
)


class TeamSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    leader = serializers.CharField(source='leaderinteam.leader')

    class Meta:
        model = Team
        fields = 'name', 'leader',


class PositionSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    class Meta:
        model = Position
        fields = '__all__'


class CompetenceSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    class Meta:
        model = Competence
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    competence = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Skill
        fields = 'name', 'domain', 'competence'


class RaitingSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    class Meta:
        model = Rating
        fields = (
            'score', 'date_score', 'need_to_study',
            'date_need', 'date_start', 'date_end', 'match', 'chief_proof',
        )


class LastRatingSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    rating = RaitingSerializer(read_only=True, many=True)
    skill = SkillSerializer(read_only=True,)

    class Meta:
        model = LastRating
        fields = 'skill', 'last_match', 'last_date', 'rating'


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    position = serializers.StringRelatedField(read_only=True)
    lastrating = LastRatingSerializer(many=True, read_only=True)
    team = TeamSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'date_hire', 'date_fire', 'team',
            'position', 'grade', 'role', 'key_people', 'bus_factor', 'emi',
            'lastrating',
        )


class CandidateSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    class Meta:
        model = Candidate
        fields = 'link',


class VacancySerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""
    team = serializers.StringRelatedField(read_only=True)
    position = serializers.StringRelatedField(read_only=True)
    candidate = CandidateSerializer(read_only=True, many=True)

    class Meta:
        model = Vacancy
        fields = 'position', 'team', 'closed', 'candidate',


class UserInTeamSerializer(serializers.ModelSerializer):
    """Сериалайзер модели."""
    position = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = User
        fields = 'id', 'last_name', 'first_name', 'position',


class VacancyInTeamSerializer(serializers.ModelSerializer):
    """Сериалайзер модели."""
    position = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Vacancy
        fields = 'id', 'position', 'closed',



class TeamMemberSerializer(serializers.ModelSerializer):
    """Сериалайзер модели.
    
    UserInTeamSerializer -> UserSerializer
    VacancyInTeamSerializer -> VacancySerializer
    """
    user = UserInTeamSerializer(many=True, read_only=True)
    vacancy = VacancyInTeamSerializer(many=True, read_only=True)
    leader = serializers.CharField(source='leaderinteam.leader')

    class Meta:
        model = Team
        fields = (
            'name', 
            'leader', 
            'user',
            'vacancy',
        )
