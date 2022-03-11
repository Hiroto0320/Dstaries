from django import forms
from .models import User, DiaryContent
from django.contrib.auth.password_validation import validate_password
class IconForm(forms.ModelForm):
    icon = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('icon',)

class BackgroundImageForm(forms.ModelForm):
    background_image = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('background_image',)

class AttachedImageForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.FileInput, label='You can attach a photo.')
    class Meta:
        model = DiaryContent
        fields = ('photo',)