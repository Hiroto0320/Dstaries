from django import forms
from .models import User, DiaryContent
from django.contrib.auth.password_validation import validate_password
class ImageForm(forms.ModelForm):
    icon = forms.ImageField(required=False, widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('icon',)

class AttachedImageForm(forms.ModelForm):
    photo = forms.ImageField(required=False, widget=forms.FileInput, label='You can attach a photo.')
    class Meta:
        model = DiaryContent
        fields = ('photo',)