from api.views import (CandidateViewSet, ChoiceListSet, CompetenceViewSet,
                       FilterList, LastRatingViewSet, PositionViewSet,
                       RatingViewSet, SkillViewSet, TeamMemberViewSet,
                       TeamViewSet, UserViewSet, VacancyViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()
router_v1.register('team', TeamViewSet, basename='team')
router_v1.register('teammember', TeamMemberViewSet, basename='teammember')
router_v1.register('competence', CompetenceViewSet, basename='competence')
router_v1.register('skill', SkillViewSet, basename='skill')
router_v1.register('rating', RatingViewSet, basename='rating')
router_v1.register('lastrating', LastRatingViewSet, basename='lastrating')
router_v1.register('user', UserViewSet, basename='user')
router_v1.register('candidate', CandidateViewSet, basename='candidate')
router_v1.register('vacancy', VacancyViewSet, basename='vacancy')
router_v1.register('position', PositionViewSet, basename='position')


urlpatterns = [
    path('v1/', include(router_v1.urls), name='api-root'),
    path('v1/choice/', ChoiceListSet.as_view(), name='choice-list'),
    path('v1/filter/', FilterList.as_view(), name='filter'),
]
