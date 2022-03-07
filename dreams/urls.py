from django.urls import path
from . import views

app_name = 'dreams'

urlpatterns = [
    path('', views.home, name='home'),
    path('dreams/', views.dreams, name='dreams'),
]