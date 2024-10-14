from api.serializers import (CandidateSerializer, CompetenceSerializer,
                             LastRatingSerializer, PositionSerializer,
                             RaitingSerializer, SkillSerializer,
                             TeamMemberSerializer, TeamSerializer,
                             UserSerializer, VacancySerializer,
                             FilterSerializer, ChoiceListSerializer)
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from employee.constants import GRADE, MONTH, P_COUNT
from employee.models import (Candidate, Competence, LastRating, Position,
                             Rating, Skill, Team, User, Vacancy)
from rest_framework import filters, generics, viewsets


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели пользователи(сотрудники)

    -- http://starsmap.ddns.net:8000/api/v1/user/?first_name=Роберт&last_name=Акимов
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
#    permission_classes = (IsAdmin, )
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id',)
    filterset_fields = ('id', 'username', 'first_name', 'last_name')


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели команда

    -- -- http://starsmap.ddns.net:8000/api/v1/team/?name=Медиа
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', 'name')
    filterset_fields = ('id', 'name',)


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели члены команды

    -- http://starsmap.ddns.net:8000/api/v1/teammember/?name=Медиа
    """

    queryset = Team.objects.all()
    serializer_class = TeamMemberSerializer
    filter_backends = (filters.SearchFilter,)
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', 'name')
    filterset_fields = ('id', 'name')


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели компетенции

    -- http://starsmap.ddns.net:8000/api/v1/competence/?name=Знание%20иностранных%20языков
    """
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', 'name')
    filterset_fields = ('id', 'name',)


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели навыки

    -- http://starsmap.ddns.net:8000/api/v1/skill/?name=Китайский%20язык
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', 'name', 'competence', 'domain')
    filterset_fields = ('id', 'name', 'competence', 'domain')


class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели оценок на каждую дату аттестации

    -- http://starsmap.ddns.net:8000/api/v1/rating/?score=5
    """
    queryset = Rating.objects.all()
    serializer_class = RaitingSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', 'score', 'date_score', 'match', 'need_to_study')
    filterset_fields = ('id', 'score', 'date_score', 'match', 'need_to_study')


class LastRatingViewSet(viewsets.ModelViewSet):
    """Вьюсет модели последняя оценка сотрудника с прицепом временных оценок

    -- http://starsmap.ddns.net:8000/api/v1/lastrating/?user=1&skill=1
    """

    queryset = LastRating.objects.all()
    serializer_class = LastRatingSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = (
        'id', 'user', 'skill', 'last_score', 'last_date', 'last_match',
    )
    filterset_fields = (
        'id', 'user', 'skill', 'last_score', 'last_date', 'last_match',
    )
    http_method_names = ['get', 'patch']


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели ссылки HH.RU для вакансий"""

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели вакансии

    -- http://starsmap.ddns.net:8000/api/v1/vacancy/?team=1
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('position', 'team')


class FilterList(generics.ListAPIView):
    """
    Возвращает данные по команде с наложением вариантов фильтров и количественными счетчиками

    count - подсчитывает количество сотрудников в команде
    position_count - подсчитывает количество должностей в команде
    key_count - подсчитывает количество key сотрудников в команде
    bus_count - подсчитывает количество bus сотрудников в команде
    match_count, nomatch_count - подсчитывает количество соответствий навыков


    param1 -- -- http://starsmap.ddns.net:8000/api/v1/filter/?team_id=1&user_id=2&skill_id=1
    param2 -- -- http://starsmap.ddns.net:8000/api/v1/filter/?user_id=1&skill_id=1 (team_id=1 by default)
    param3 -- -- http://starsmap.ddns.net:8000/api/v1/filter/?team_id=3&competence_id=1 (skill&competence don't work together)
    param4 -- -- http://starsmap.ddns.net:8000/api/v1/filter/?team_id=2&grade=Middle (grade_id=grade but working grade)
    param5 -- -- http://starsmap.ddns.net:8000/api/v1/filter/?team_id=4&month_id=0 (comming soon, now only today)
    """

    model = User
    serializer_class = FilterSerializer
    filter_fields = (
        'team_id',
        'user_id',
        'grade',
    )

    def get_queryset(self):
        queryset = User.objects.all()
        user_id = self.request.query_params.get('user_id', )
        team_id = self.request.query_params.get('team_id', 1)
        grade = self.request.query_params.get('grade')
        skill_id = self.request.query_params.get('skill_id')
        competence_id = self.request.query_params.get('competence_id')
        queryset = queryset.filter(team=team_id,)
        if user_id:
            queryset = queryset.filter(id=user_id, team=team_id,)

        if grade:
            queryset = queryset.filter(grade=grade,)
        if skill_id:
            queryset = queryset.filter(
                lastrating__skill__id=skill_id,
                lastrating__last_match=True,
            )
        if competence_id and (not skill_id):
            queryset = queryset.filter(
                lastrating__skill__competence_id=competence_id,
                lastrating__last_match=True,
            )
        P_COUNT.clear()
        return queryset


class ChoiceListSet(generics.ListAPIView):
    """Список возможных выборов(наполнение дропдаун меню на фронте) для фильтра в api/v1/filter.

    -- http://starsmap.ddns.net:8000/api/v1/choice/
    """

    def get_serializer_class(self):
#        return 'fake_stub_serializer'
        return ChoiceListSerializer

    def list(self, *args, **kwargs):
        team = {}
        teams = Team.objects.all()
        for each_team in teams:
            team[each_team.id] = each_team.name

        competence = {}
        competences = Competence.objects.all()
        for each_competence in competences:
            competence[each_competence.id] = each_competence.name

        skill = {}
        skills = Skill.objects.all()
        for each_skill in skills:
            skill[each_skill.id] = each_skill.name

        grade = dict(GRADE)
        month = MONTH
        choices = [
            {'team': team}, {'competence': competence}, {'skill': skill},
            {'month': month}, {'grade': grade},
        ]
        return JsonResponse(data={
            'choices': choices
        })


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели должность"""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
