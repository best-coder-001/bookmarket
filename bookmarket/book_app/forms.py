from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django.contrib.auth.models import User


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = "__all__"
        widgets = {
            "TODO: Implement me..."
        }


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']