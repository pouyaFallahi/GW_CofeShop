from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

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
