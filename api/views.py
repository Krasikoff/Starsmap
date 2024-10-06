from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import (
    CompetenceSerializer, LastRatingSerializer, RaitingSerializer,
    SkillSerializer, TeamSerializer, UserSerializer, VacancySerializer,
    CandidateSerializer,
)
from employee.models import (
    Competence, LastRating, Rating, Skill, Team, User, Vacancy, Candidate,
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
#    lookup_field = 'id'
#    permission_classes = (IsAdmin, )
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('username',)


class TeamViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('name', 'leader')


class CompetenceViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('name',)


class SkillViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = (filters.SearchFilter, )
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('id', )
    filterset_fields = ('name', 'domain')


class RatingViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = Rating.objects.all()
    serializer_class = RaitingSerializer
    http_method_names = ['get',]


class LastRatingViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = LastRating.objects.all()
    serializer_class = LastRatingSerializer
    http_method_names = ['get',]


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
