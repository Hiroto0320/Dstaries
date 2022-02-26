from django import forms
from .models import User
from django.contrib.auth.password_validation import validate_password
class ImageForm(forms.ModelForm):
    icon = forms.FileField(required=False)
    class Meta:
        model = User
        fields = ('icon',)