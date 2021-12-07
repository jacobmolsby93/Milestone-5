from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_styles, name='styles'),
    path('<int:style_id>/', views.style_detail, name='style_detail'),
    path('add/', views.add_style, name='add_style'),
]