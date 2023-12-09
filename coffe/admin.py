from django.contrib import admin
from .models import Customer,Staff,Manager
# Register your models here.
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Manager)
