from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import (
    CompetenceSerializer, LastRatingSerializer, RaitingSerializer,
    SkillSerializer, TeamSerializer, UserSerializer, VacancySerializer,
    CandidateSerializer, TeamMemberSerializer,
)
from employee.models import (
    Competence, LastRating, Rating, Skill, Team, User, Vacancy, Candidate,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели
    
    http://localhost:8000/api/v1/user/?first_name=Роберт&last_name=Акимов
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
#    permission_classes = (IsAdmin, )
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id',)
    filterset_fields = ('username', 'first_name', 'last_name')


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели
    
    http://localhost:8000/api/v1/team/?name=Медиа
    """

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('name',)


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели
    
    http://localhost:8000/api/v1/team/?name=Медиа
    """

    queryset = Team.objects.all()
    serializer_class = TeamMemberSerializer
    filter_backends = (filters.SearchFilter,)
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('name',)



class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('name',)


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('name', 'domain')


class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = Rating.objects.all()
    serializer_class = RaitingSerializer
#    http_method_names = ['get',]


class LastRatingViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = LastRating.objects.all()
    serializer_class = LastRatingSerializer


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('position', 'team')
