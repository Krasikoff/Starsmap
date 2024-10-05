from rest_framework import viewsets
#from django_filters.rest_framework import DjangoFilterBackend

from api.serializers import (CompetenceSerializer, LastRatingSerializer,
                             RaitingSerializer, SkillSerializer,
                             TeamSerializer, UserSerializer)
from employee.models import (Competence, LastRating, Rating,
                             Skill, Team, User)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет модели"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
#    lookup_field = 'id'
#    permission_classes = (IsAdmin, )
#    filter_backends = (filters.SearchFilter, )
#    filter_backends = (DjangoFilterBackend,)
#    search_fields = ('id', )
#    http_method_names = ['get',]
#    filterset_fields = ('username',)


class TeamViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get',]


class CompetenceViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    http_method_names = ['get',]


class SkillViewSet(viewsets.ModelViewSet):
    """Вьюсет модели"""

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get',]


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
