from django.urls import path

from . import views

app_name = 'rating'

urlpatterns = [
    path('', views.rating_list, name='rating_list'),
    path('<int:pk>/', views.rating_detail, name='rating_detail'),
]
