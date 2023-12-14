from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import MyUser


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['phone', ]


class CustomerCreationModelForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'gender', 'address', 'username', 'password' ]
