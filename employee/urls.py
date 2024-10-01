from django.urls import path

from .views import employee_list, employee_detail

urlpatterns = [
    path('api/v1/employee/', employee_list),
    path('api/v1/employee/<int:pk>/', employee_detail)
]
