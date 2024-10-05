from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (CompetenceViewSet, LastRatingViewSet, RatingViewSet,
                       SkillViewSet, TeamViewSet, UserViewSet)

router_v1 = DefaultRouter()
router_v1.register('team', TeamViewSet, basename='team')
router_v1.register('competence', CompetenceViewSet, basename='competence')
router_v1.register('skill', SkillViewSet, basename='skill')
router_v1.register('rating', RatingViewSet, basename='rating')
router_v1.register('lastrating', LastRatingViewSet, basename='lastrating')
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls), name='api-root'),
]
