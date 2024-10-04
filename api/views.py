from django.shortcuts import render
from api.serializers import (UserSerializer, TeamSerializer, SkillSerializer, RaitingSerializer)
from rest_framework import permissions as main_permissions
from rest_framework import response, status, views, viewsets

from employee.models import User, Team, Competence, Skill, Rating


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
    serializer_class = TeamSerializer
    http_method_names = ['get',]


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get',]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
#    lookup_field = 'user'
    serializer_class = RaitingSerializer
    http_method_names = ['get',]
