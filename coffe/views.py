from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView
from .models import Category,Comment,CustomerOrder,Item,SellRecord,User
from django.urls import reverse_lazy
# Create your views here.
class ItemListView(ListView):
    model=Item
    template_name="coffe/itemlist.html"
    context_object_name="items"
class ItemCreateView(CreateView):
    model=Item
    fields="__all__"
    template_name="coffe/create_item.html"
class ItemUpdateView(UpdateView,):
    model=Item
    fields="__all__"
    success_url="coffe:list_item"
class ItemDeleteView(DeleteView):
    models=Item
    success_url = reverse_lazy("list_item")
    




