from django.urls import path
from . import views

app_name = 'dreams'

urlpatterns = [
    path('', views.home, name='home'),
    # path('users/', views.search_by_dream, name='search_by_dream'),
]