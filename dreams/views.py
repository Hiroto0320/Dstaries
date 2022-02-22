from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User

app_name = 'dreams'

# Create your views here.
def home(request):
    users = User.objects.all().order_by('joined_date')
    data = {
        'users':users
    }
    return render(request, 'dreams/home.html', data)

# def search_by_dream(request):
#     users = User.objects.all()
#     data = {
#         'users':users,
#     }
#     return render(request, 'dreams/users.html', data)