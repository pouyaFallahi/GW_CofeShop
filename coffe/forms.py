from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views import View

from .models import MyUser
from django import forms


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['phone', ]


class CustomerCreationModelForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'gender', 'email', 'phone', 'username', 'password', 'address']


class LoginUser(View):
    template_name = 'login.html'
    error_message = forms.CharField(widget=forms.HiddenInput(), required=False)

