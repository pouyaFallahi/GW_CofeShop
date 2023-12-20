from django.contrib import admin
from .models import MyUser, Category, Item
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Category)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_preview']
    readonly_fields=['thumbnail_preview']
    def thumbnail_preview(self,obj):
        return obj.thumbnail_preview
    thumbnail_preview.short_description='preview'
    thumbnail_preview.allow_tags=True
    
admin.site.register(Item, ItemAdmin)
