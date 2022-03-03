from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign/', views.sign, name='sign'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('user_detail/<int:id>', views.user_detail, name='user_detail'),
    path('diary/<int:id>', views.diary, name='diary'),
    path('diary_content/<int:diary_id>', views.diary_content, name='diary_content'),
    path('keep_diary/', views.keep_diary, name='keep_diary'),
    path('message/<int:id>/', views.message, name='message'),
    path('api/good/<int:id>', views.ApiGood, name="api_good"),
]