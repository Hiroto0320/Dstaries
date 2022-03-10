from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    favorite = models.CharField(max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    icon = models.ImageField(upload_to='icons/', null=False, default='icons/default_jjjs8l.png')
    joined_date = models.DateField(auto_now_add=True)
    introduction = models.CharField(max_length=450, blank=True)
    dream = models.CharField(max_length=125, blank=True)
    task = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    Actively_point = models.IntegerField(default=0)
    is_public = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'

class DiaryTitle(models.Model):
    diary_title = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='related_diary_title'
    )
    is_public = models.BooleanField(default=True)
    goodstamp = models.IntegerField(default=0)
    class Meta:
        db_table = 'diary_title'

    def __str__(self):
        return self.diary_title

class DiaryContent(models.Model):
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE)
    diary_title = models.ForeignKey(
        'DiaryTitle', on_delete=models.CASCADE)
    content = models.CharField(max_length=700, blank=True)
    photo = models.ImageField(upload_to='attached_photo/', null=True)
    subtitle = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'diary_content'

class Thread(models.Model):
    user1 = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='thread_sender')
    user2 = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='thread_receiver')

    class Meta:
        db_table = 'thread'
    
    def __str__(self):
        return f'{self.user1} : {self.user2}'

class Message(models.Model):
    thread = models.ForeignKey(
        'Thread', on_delete=models.CASCADE)
    sender = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='message_sender')
    receiver = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='message_receiver')
    content = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True)
    # is_read = models.BooleanField(default=False)

    class Meta:
        db_table = 'message'

# class Like(models.Model):
#     following = models.ForeignKey(
#         'User', on_delete=models.CASCADE, related_name='like')
#     Liked = models.ForeignKey(
#         'User', on_delete=models.CASCADE, related_name='liked')

#     class Meta:
#         db_table = 'user_like'