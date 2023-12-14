from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Category, Comment, CustomerOrder, Item, SellRecord, MyUser
from django.urls import reverse_lazy
from .forms import CustomerCreationModelForm
from django.contrib.auth.views import LoginView


# Create your views here.


class CustomerSignupView(CreateView):
    model = MyUser
    template_name = 'coffe/customer_create.html'
    form_class = CustomerCreationModelForm
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     form.instance.is_customer = self.request.user
    #     return super().form_valid(form)


class LoginView(LoginView):
    template_name = 'coffe/login.html'
    success_url = reverse_lazy('list_item')  # Change in the future


class CustomerListView(ListView):
    model = MyUser
    fields = '__all__'
    context_object_name = 'customers'

    # def get_queryset()
    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(is_customer=True)


class ItemListView(ListView):
    model = Item
    template_name = "coffe/itemـlist.html"
    context_object_name = "items"


class ItemCreateView(CreateView):
    model = Item
    fields = "__all__"
    template_name = "coffe/create_item.html"


class ItemUpdateView(UpdateView, ):
    model = Item
    fields = "__all__"
    success_url = "coffe:list_item"


class ItemDeleteView(DeleteView):
    models = Item
    success_url = reverse_lazy("list_item")
