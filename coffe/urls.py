from django.urls import path
from .views import *

app_name="coffe"

urlpatterns = [
    path('item/list/', ItemListView.as_view(),name="list_item"),
    path("item/create/",ItemCreateView.as_view(),name="create_item"),
    path("item/<int:pk>/update/",ItemUpdateView.as_view(),name="update_item"),
    path("item/<int:pk>/delete/",ItemDeleteView.as_view(),name="delete_item"),
    path("user/signup/", CustomerSignupView.as_view(), name="signup_user"),
    
]