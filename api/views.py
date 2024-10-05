# from django.shortcuts import render
from rest_framework import viewsets

from api.serializers import (CompetenceSerializer, LastRatingSerializer,
                             RaitingSerializer, SkillSerializer,
                             TeamSerializer, UserSerializer)
from employee.models import (Competence, LastRating, Rating,
                             Skill, Team, User)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#    lookup_field = 'id'
#    permission_classes = (IsAdmin, )
#    filter_backends = (filters.SearchFilter, )
#    search_fields = ('id', )
    http_method_names = ['get',]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    http_method_names = ['get',]


class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    http_method_names = ['get',]


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get',]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RaitingSerializer
    http_method_names = ['get',]


class LastRatingViewSet(viewsets.ModelViewSet):
    queryset = LastRating.objects.all()
    serializer_class = LastRatingSerializer
    http_method_names = ['get',]
