from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Manager, Staff


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Customer
        fields = ['phone', ]


class StaffCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Staff
        fields = ['phone', ]


class ManagerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Manager
        fields = ['phone', ]
