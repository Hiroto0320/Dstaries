from django.contrib import admin
from .models import User, DiaryTitle, DiaryContent, Message, Thread
# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email','is_active', 'is_staff', 'joined_date', 'Actively_point')
    list_display_links = ('username', 'email')
admin.site.register(User, AdminUser)

class AdminDiary(admin.ModelAdmin):
    list_display = ('user', 'diary_title', 'date')
    list_display_links = ('user', 'diary_title', 'date')
admin.site.register(DiaryTitle, AdminDiary)

class AdminDiaryContent(admin.ModelAdmin):
    list_display = ('diary_title', 'user', 'date')
admin.site.register(DiaryContent, AdminDiaryContent)

class AdminMessage(admin.ModelAdmin):
    list_display = ('receiver', 'sender', 'date')
admin.site.register(Message, AdminMessage)

admin.site.register(Thread)