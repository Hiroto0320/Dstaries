from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.db.models import Q

app_name = 'dreams'

# Create your views here.
def home(request):
    users = User.objects.all().order_by('joined_date')
    data = {
        'users':users
    }
    return render(request, 'dreams/home.html', data)

def dreams(request):
    dreamers = User.objects.exclude(Q(dream__exact="")|Q(is_public=False))
    data = {
        'dreamers':dreamers,
    }
    return render(request, 'dreams/dreams.html', data)