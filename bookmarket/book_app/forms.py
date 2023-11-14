from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import *
from django.contrib.auth.models import User


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = "__all__"
        widgets = {
            "TODO: Implement me..."
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = "__all__"


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    remember_me = forms.CharField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

class UserForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
