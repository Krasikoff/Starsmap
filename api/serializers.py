from rest_framework import serializers

from employee.models import (Competence, LastRating, Position,
                             Rating, Skill, Team, User)


class TeamSerializer(serializers.ModelSerializer):
    leader = serializers.CharField(source='leaderinteam.leader')

    class Meta:
        model = Team
        fields = 'name', 'leader'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competence
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    competence = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Skill
        fields = 'name', 'domain', 'competence'


class RaitingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = (
            'score', 'date_score', 'need_to_study',
            'date_need', 'date_start', 'date_end', 'match', 'chief_proof',
        )


class LastRatingSerializer(serializers.ModelSerializer):
    rating = RaitingSerializer(read_only=True, many=True)
    skill = SkillSerializer(read_only=True,)

    class Meta:
        model = LastRating
        fields = 'skill', 'last_match', 'last_date', 'rating'


class UserSerializer(serializers.ModelSerializer):
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
