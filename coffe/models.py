from django.db import models
from users.models import CustomUser


# Create your models here.
class User(models.Model):
    differentـgender = {
        "F": "Famle",
        "M": "Male",
        "o": "other"}
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=1, choices=differentـgender)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(
        blank=False, null=False, unique=True, max_length=100)
    password = models.CharField(blank=False, null=False, max_length=50)

    @property
    def full_name(self):
        return f'{self.first_name}-{self.last_name}'

    class Meta:
        abstract = True


class Customer(User):
    def __str__(self):
        return f"{self.full_name}"


class Staff(User):
    roles = {"B": "Barista",
             "C": "Cashier",
             "A": "Accountant",
             "S": " Server"}
    role = models.CharField(max_length=1, choices=roles)

    def __str__(self):
        return f"{self.full_name}"


class Manager(User):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="managers"
    )

    def __str__(self):
        return f"{self.full_name}"


class Customer(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Staff(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Manager(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Category(models.Model):
    category_names = [('COLD_DRINKS', 'cold_drinks'), ('HOT_DRINKS', 'hot_drinks'), ('FOOD', 'food')]
    name = models.CharField(choices=category_names, max_length=15, null=False, default='HOT_DRINKS')


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=150, null=False, unique=True)
    price = models.FloatField(null=False)

    def __str__(self):
        return f"{self.name}"


class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_order')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='customer_order')
    item = models.ManyToManyField(Item, related_name="customer_orders")
    item_quantity = models.IntegerField(default=0)
    total_amount = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Sell_Record(models.Model):
    order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='sell_record')
    date = models.DateTimeField(auto_now=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='sell_record')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='sell_record')
