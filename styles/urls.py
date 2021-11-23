from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_styles, name='styles'),
    path('<style_id>', views.style_detail, name='style_detail'),
]