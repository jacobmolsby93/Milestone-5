from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('service_request/<service_id>/', views.service_request, name="service_request"),
]