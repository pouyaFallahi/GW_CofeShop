from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Customer, Manager, Staff
from django.views.generic import CreateView
from .forms import CustomerCreationForm
from django.contrib.auth.models import Group


# Create your views here.
class CustomerSignupView(CreateView):
    model = Customer
    template_name = ''
    success_url = reverse_lazy('login')
    form_class = CustomerCreationForm

    def form_valid(self, form):
        user = form.save()
        customer_group = Group.objects.get(name='Customer')
        user.groups.add(customer_group)
        return super().form_valid(form)


class StaffSignupView(CreateView):
    model = Staff
    template_name = ''
    success_url = reverse_lazy('login')
    form_class = StaffCreationForm

    def form_valid(self, form):
        user = form.save()
        staff_group = Group.objects.get(name='Staff')
        user.groups.add(staff_group)
        return super().form_valid(form)


class ManagerSignupView(CreateView):
    model = Manager
    template_name = ''
    success_url = reverse_lazy('login')
    form_class = ManagerCreationForm

    def form_valid(self, form):
        user = form.save()
        manager_group = Group.objects.get(name='Manager')
        user.groups.add(manager_group)
        return super().form_valid(form)
