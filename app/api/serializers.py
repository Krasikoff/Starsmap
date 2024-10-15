from django.utils import timezone as tz
from django.core.exceptions import ValidationError
from employee.constants import P_COUNT
from employee.models import (Candidate, Competence, LastRating, Position,
                             Rating, Skill, Team, User, Vacancy)
from rest_framework import serializers


class IncrSrlz(serializers.Serializer):
    _incr = 0
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        self._incr += 1
        return self._incr


class TeamSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    leader = serializers.CharField(source='leaderinteam.leader')

    class Meta:
        model = Team
        fields = 'id', 'name', 'leader',


class PositionSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    users_count = serializers.IntegerField(source='user.count', read_only=True,)
    incr_nmbr = IncrSrlz(read_only=True)

    class Meta:
        model = Position
        fields = 'incr_nmbr', 'name', 'users_count'


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
        fields = 'id', 'name', 'domain', 'competence'


class RaitingSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    class Meta:
        model = Rating
        fields = (
            'id', 'score', 'date_score', 'need_to_study',
            'date_need', 'date_start', 'date_end', 'match', 'chief_proof',
        )


class LastRatingSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    rating = RaitingSerializer(read_only=True, many=True)
    skill = SkillSerializer(read_only=True,)

    class Meta:
        model = LastRating
        fields = (
            'id', 'skill', 'last_score',
            'last_match', 'last_date', 'last_score', 'last_need_to_study',
            'last_date_study', 'rating'
        )

    def update(self, instance, validated_data):
        for attr in validated_data:
            if attr == 'last_need_to_study':
                instance.last_date_study = tz.now().date()
            else:
                raise ValidationError(
                    'Разрешено изменение только поля last_need_to_study'
                )
        return super().update(instance, validated_data)


class ShortLastRatingSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    _incr_match = 0
    _incr_nomatch = 0
    skill = SkillSerializer(read_only=True,)
    match_count = serializers.SerializerMethodField()
    nomatch_count = serializers.SerializerMethodField()

    class Meta:
        model = LastRating
        fields = (
            'match_count', 'nomatch_count', 'id', 'skill', 'last_score',
            'last_match', 'last_date', 'last_score', 'last_need_to_study',
            'last_date_study'
        )

    def get_match_count(self, obj):
        if obj.last_match:
            self._incr_match += 1
        return self._incr_match

    def get_nomatch_count(self, obj):
        if not obj.last_match:
            self._incr_nomatch += 1
        return self._incr_nomatch


class UserSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    _incr = 0
    position = serializers.CharField(read_only=True)
    lastrating = LastRatingSerializer(many=True, read_only=True)
    team = TeamSerializer(many=True, read_only=True)
    count = serializers.SerializerMethodField()
    position_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'count', 'id', 'first_name', 'last_name', 'date_hire', 'date_fire', 'team',
            'position', 'position_count', 'grade', 'role', 'key_people', 'bus_factor', 'emi',
            'lastrating',
        )

    p_count = P_COUNT

    def get_position_count(self, obj):
        if obj.position in self.p_count:
            self.p_count[obj.position] += 1
        else:
            self.p_count[obj.position] = 1
        return self.p_count[obj.position]

    def get_count(self, obj):
        self._incr += 1
        return self._incr


class FilterSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""

    _incr = 0
    _incr_key = 0
    _incr_bus = 0

    position = serializers.CharField(read_only=True)
    lastrating = ShortLastRatingSerializer(many=True, read_only=True)
    team = TeamSerializer(many=True, read_only=True)
    count = serializers.SerializerMethodField()
    position_count = serializers.SerializerMethodField()
    key_count = serializers.SerializerMethodField()
    bus_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'count', 'id', 'first_name', 'last_name', 'date_hire', 'date_fire', 'team',
            'position', 'position_count', 'grade', 'role', 'key_people', 'key_count', 'bus_factor', 'bus_count', 'emi',
            'lastrating',
        )

    p_count = P_COUNT

    def get_position_count(self, obj):
        if obj.position in self.p_count:
            self.p_count[obj.position] += 1
        else:
            self.p_count[obj.position] = 1
        return self.p_count[obj.position]

    def get_count(self, obj):
        self._incr += 1
        return self._incr

    def get_key_count(self, obj):
        if obj.key_people:
            self._incr_key += 1
        return self._incr_key

    def get_bus_count(self, obj):
        if obj.bus_factor:
            self._incr_key += 1
        return self._incr_key


class VacancyCandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    """Сериалайзер модели"""
    vacancy = VacancyCandidateSerializer()

    class Meta:
        model = Candidate
        fields = 'link', 'vacancy'

    def create(self, validated_data):
        vacancy_data = validated_data.pop('vacancy', None)
        vacancy = Vacancy.objects.filter(
            position=vacancy_data['position'].id,
            team=vacancy_data['team'].id,
            closed=False
        ).first()
        if vacancy:
            validated_data['vacancy_id'] = vacancy.id
        else:
            raise ValidationError(
                f'Вакансия {vacancy_data["position"]} в команде '
                f'{vacancy_data["team"]} закрыта или другое несоответствие вводимых данных.'
            )
        return super().create(validated_data)


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


class ChoiceListSerializer(serializers.BaseSerializer):
    """stub сериалайзер"""
    pass
