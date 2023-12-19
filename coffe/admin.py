from django.contrib import admin
from .models import MyUser, Category, Item
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Category)
admin.site.register(Item)