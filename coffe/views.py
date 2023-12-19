import json
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Category, Comment, CustomerOrder, Item, SellRecord, MyUser
from django.urls import reverse_lazy
from .forms import CustomerCreationModelForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


class CustomerSignupView(CreateView):
    model = MyUser
    template_name = 'coffe/customer_create.html'
    form_class = CustomerCreationModelForm
    success_url = reverse_lazy('coffe:login')

    # def form_valid(self, form):
    #     form.instance.is_customer = self.request.user
    #     return super().form_valid(form)


class MyLoginView(LoginView):
    template_name = 'coffe/login.html'
    success_url = reverse_lazy('coffe:list_item')  # Change in the future

    def get_success_url(self):
        # چک کردن مسیر موفقیت‌آمیز و تغییر آن به مسیر مورد نظر
        if self.success_url == 'list_item':
            return reverse_lazy(self.success_url)
        return self.success_url

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('coffe:list_item')
            else:
                form.add_error(None, 'نام کاربری یا رمز عبور اشتباه است.')
        return render(request, self.template_name, {'form': form})


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


class AddToCartView(View):

    def post(self, request):
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        # Get the current cart from cookies or create a new empty cart
        cart = request.COOKIES.get('shopping_cart')
        cart = json.loads(cart) if cart else {}
        cart_item = cart.get(str(item.id), {'quantity': 0})
        cart_item['item_id'] = item.id
        cart_item['name'] = item.name
        cart_item['price'] = item.price
        cart_item['quantity'] += 1
        cart[str(item.id)] = cart_item
        response = redirect('/coffe/item/list/')
        response.set_cookie('shopping_cart', json.dumps(cart))
        messages.success(request, f'{item.name} added to the shopping cart!')
        return response


class RemoveFromCartView(View):

    def post(self, request):
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        cart = request.COOKIES.get('shopping_cart')
        cart = json.loads(cart) if cart else {}
        cart_item = cart.get(str(item.id), {'quantity': 0})
        cart_item['item_id'] = item.id
        cart_item['name'] = item.name
        cart_item['price'] = item.price
        if cart_item and cart_item['quantity'] > 0:
            cart_item['quantity'] -= 1
        cart[str(item.id)] = cart_item
        response = redirect('/coffe/item/list/')
        response.set_cookie('shopping_cart', json.dumps(cart))
        messages.success(request, f'{item.name} removed from shopping cart!')
        return response
    # def post(self, request):
    #     item_id = request.POST.get('item_id')
    #     item = get_object_or_404(Item, pk=item_id)
    #     cart = request.COOKIES.get('shopping_cart')
    #     cart = json.loads(cart) if cart else {}
    #     cart_item = cart.get(str(item.id))
    #     if cart_item and cart_item['quantity'] > 0:
    #         cart_item['quantity'] -= 1
    #     response = JsonResponse({'message': f'Quantity of {item.name} decreased in the shopping card.'})
    #     response.set_cookie('shopping_cart', json.dumps(cart))
    #     response = redirect('/coffe/item/list/')
    #     messages.success(request, f'{item.name} removed from shopping cart!')
    #     return response
class ViewShoppingCart(View):

    def get(self, request, *args, **kwargs):
        cart = request.COOKIES.get('shopping_cart', '{}')
        cart = json.loads(cart)

def show_home(request):
    return render(request, 'coffe/homepage.html')