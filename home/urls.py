from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('about-me/', views.AboutMeView, name="about-me"),
    path('contact/', views.ContactView, name='contact'),
]
