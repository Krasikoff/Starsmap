from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets

from api.serializers import (CandidateSerializer, CompetenceSerializer,
                             LastRatingSerializer, RaitingSerializer,
                             SkillSerializer, TeamMemberSerializer,
                             TeamSerializer, UserSerializer, VacancySerializer)
from employee.models import (Candidate, Competence, LastRating, Rating, Skill,
                             Team, User, Vacancy)


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


class FilterList(generics.ListAPIView):
    """
    Return a list of all with optional filtering.
    """

    model = User
    serializer_class = UserSerializer
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

        print('team_id =', team_id, 'user_id =', user_id, 'grade =', grade, 'skill_id =', skill_id)

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
        return queryset


class ChoiceList(generics.ListAPIView):
    pass
