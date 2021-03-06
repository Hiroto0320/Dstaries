from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from .models import User, DiaryTitle, DiaryContent, Message, Thread
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http.response import JsonResponse

app_name = 'accounts'

# Create your views here.

def sign(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('confirm_password'):
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            if password==confirm_password:
                try:
                    validate_password(password)
                except ValidationError as error:
                    messages.error(request, 'weak password')
                    return redirect('accounts:sign')
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'this username has already exists')
                    return redirect('accounts:sign')
                elif User.objects.filter(email=email).exists():
                    messages.error(request, 'this email has already exists')
                    return redirect('accounts:sign')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    auth.login(request, user)
                    return redirect('accounts:profile')
            
            else:
                messages.error(request, 'password does not match')
                return redirect('accounts:sign')

        else:
            email = request.POST['email']
            password = request.POST['password']
            user =auth.authenticate(email=email, password=password)
            if user:
                auth.login(request, user)
                if request.POST.get('next'):
                    return redirect(request.POST['next'])
                else:
                    return redirect('dreams:home')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('accounts:sign')
    else:
        return render(request, 'accounts/sign.html')

def signout(request):
    auth.logout(request)
    return redirect('dreams:home')

@login_required(login_url='accounts:sign')
def profile(request):
    icon_form = forms.IconForm(request.POST or None, request.FILES or None, instance=request.user)
    background_image_form = forms.BackgroundImageForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == "POST":
        if request.POST.get('username'):
            if icon_form.is_valid():
                icon_form.save(commit=True)
            if background_image_form.is_valid():
                background_image_form.save(commit=True)
            User.objects.filter(username=request.user.username, email=request.user.email).update(
            username=request.POST.get('username'),
            favorite=request.POST.get('favorite'),
            task=request.POST.get('task'),
            dream=request.POST.get('dream'),
            introduction=request.POST.get('about'),
            website=request.POST.get('website'),
            is_public=request.POST.get('is_public-account'),
            )
        if request.POST.get('delete_message-room_user1'):
            Thread.objects.filter(user2=request.user, user1=request.POST.get('delete_message-room_user1')).delete()
        if request.POST.get('delete_message-room_user2'):
            Thread.objects.filter(user1=request.user, user2=request.POST.get('delete_message-room_user2')).delete()
        User.objects.filter(email=request.user.email).update(
            Actively_point=DiaryContent.objects.filter(user=request.user).count()
        )
        return redirect('accounts:profile')
    return render(request, 'accounts/profile.html', context={
        'icon_form':icon_form,
        'background_image_form':background_image_form,
    })

@login_required(login_url='accounts:sign')
def user_detail(request, id):
    user_detail = get_object_or_404(User, pk=id)
    if (request.user != user_detail) and (not user_detail.is_public):
        return redirect('dreams:home')
    data = {
        'user_detail': user_detail
    }
    return render(request, 'accounts/user_detail.html', data)

@login_required(login_url='accounts:sign')
def diary(request, id):
    user = get_object_or_404(User, pk=id)
    if (request.user != user) and (not user.is_public):
        return redirect('dreams:home')
    diaries = DiaryTitle.objects.filter(user=id).order_by('id')
    data = {
        'diaries': diaries,
        'id': id,
    }
    return render(request, 'accounts/diaries.html', data)

@login_required(login_url='accounts:sign')
def diary_content(request, diary_id):
    title = get_object_or_404(DiaryTitle, id=diary_id)
    contents = DiaryContent.objects.filter(diary_title=diary_id).order_by('date')
    if title.user == request.user or title.is_public:
        data = {
            'contents': contents,
            'title':title,
        }
        return render(request, 'accounts/diary_content.html', data)
    else:
        messages.error(request, 'You can not enter.')
        return redirect('dreams:home')

@login_required(login_url='accounts:sign')
def keep_diary(request):
    diaries = DiaryTitle.objects.filter(user=request.user)
    contents = DiaryContent.objects.filter(user=request.user)
    # photo_form = forms.AttachedImageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if request.POST.get('create_diary-title'):
            if not DiaryTitle.objects.filter(user=request.user, diary_title=request.POST.get('create_diary-title')).exists():
                DiaryTitle.objects.filter(user=request.user).create(
                    diary_title=request.POST.get('create_diary-title'),
                    user=request.user,
                    is_public=request.POST.get('is_public'),
                )
        if request.POST.get('delete_diary-title'):
            DiaryTitle.objects.filter(user=request.user, diary_title=request.POST.get('delete_diary-title')).delete()

        if request.POST.get('delete_diary-content'):
            DiaryContent.objects.filter(id=request.POST.get('delete_diary-content'), user=request.user).delete()
        
        if request.POST.get('diary-title'):
            title = diaries.get(diary_title=request.POST.get('diary-title'))
            new_content = DiaryContent.objects.filter(user=request.user).create(
                diary_title=title,
                user=request.user,
                content=request.POST.get('content'),
                subtitle=request.POST.get('diary-subtitle'),
            )
            form = forms.AttachedImageForm(request.POST or None, request.FILES or None, instance=new_content)
            if form.is_valid():
                form.save(commit=True)
        User.objects.filter(email=request.user.email).update(
        Actively_point=DiaryContent.objects.filter(user=request.user).count()
        )
        return redirect('accounts:keep_diary')
    return render(request, 'accounts/keep_diary.html', context={
        'diaries': diaries,
        'contents': contents,
        # 'photo_form':photo_form,
    })

@login_required(login_url='accounts:sign')
def message(request, id):
    friend = get_object_or_404(User, pk=id)
    if (request.user == friend) or (not friend.is_public):
        messages.error(request, 'You can not enter.')
        return redirect('dreams:home')
    if request.method == 'POST':
        try:
            thread = get_object_or_404(Thread, user1=request.user, user2=friend)
        except:
            try:
                thread = get_object_or_404(Thread, user1=friend, user2=request.user)
            except:
                thread = Thread.objects.create(
                    user1=request.user,
                    user2=friend
                )
        Message.objects.filter(sender=request.user, receiver=friend).create(
            thread=thread,
            sender=request.user,
            receiver=friend,
            content=request.POST.get('message'),
        )
    to_me_messages = Message.objects.filter(receiver=request.user, sender=friend).order_by('date')
    from_me_messages = Message.objects.filter(sender=request.user, receiver=friend).order_by('date')
    direct_messages = to_me_messages|from_me_messages
    data = {
        'direct_messages':direct_messages,
        'friend':friend,
    }
    return render(request, 'accounts/message.html', data)

def ApiGood(request, id):
    try:
        obj = DiaryTitle.objects.get(id=id)
    except DiaryTitle.DoesNotExist:
        raise Http404
    obj.goodstamp += 1
    obj.save()

    return JsonResponse({"goodstamp":obj.goodstamp})