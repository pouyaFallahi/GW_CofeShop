from django.urls import path
from .views import *

app_name = "coffe"

urlpatterns = [
    path('item/list/', ItemListView.as_view(), name="list_item"),
    path("item/create/", ItemCreateView.as_view(), name="create_item"),
    path("item/<int:pk>/update/", ItemUpdateView.as_view(), name="update_item"),
    path("item/<int:pk>/delete/", ItemDeleteView.as_view(), name="delete_item"),
    path("user/signup/", CustomerSignupView.as_view(), name="signup_user"),
    path("user/login/", MyLoginView.as_view(), name='login'),
    path('user/logout', MyLogoutView.as_view(), name='logout'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('', show_home.as_view(), name='home'),
    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('shopingCart/', ViewShoppingCart.as_view(), name='shopping_cart'),
]
