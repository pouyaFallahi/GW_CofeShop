from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=12)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(blank=False, null=False, unique=True,max_length=100)
    password = models.CharField(blank=False, null=False, max_length=50)

    class Meta:
        abstract = True


class Customer(User):
    customer_id = models.AutoField(primary_key=True, default=1, null=False)
    def __str__(self):
        return f"{self.first_name} -{self.last_name}"


class Staff(User):
    staff_id = models.AutoField(primary_key=True, default=1, null=False)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Manager(User):
    manager_id = models.AutoField(primary_key=True, default=1, null=False)
    staff_id = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="managers"
        )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Category(models.Model):
    category_names = [('COLD_DRINKS', 'cold_drinks'), ('HOT_DRINKS', 'hot_drinks'), ('FOOD', 'food')]
    category_id = models.IntegerField(serialize=True, primary_key=True)
    name = models.CharField(choices=category_names, max_length=15, null=False, default='HOT_DRINKS')
class Item(models.Model):
    item_id = models.IntegerField(serialize=True, primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item')
    name = models.CharField(max_length=150, null=False, unique=True)
    price = models.FloatField(null=False)

    def __str__(self):
        return f"{self.name}"

class CustomerOrder(models.Model):
    order_id = models.AutoField(primary_key=True, default=1, null=False)
    customer_id = models.CharField(max_length=150, null=False)
    item_id = models.CharField(max_length=150, null=False)
    quantity = models.IntegerField(default=1)
    total_amount = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='customer_order')


class ItemCustomerOrder(models.Model):
    item_customer_order_id = models.IntegerField(serialize=True, primary_key=True)
    item_id = models.ForeignKey(Item ,on_delete=models.CASCADE, related_name='item_order')
    order_id = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)


class Sell_Record(models.Model):
    order_id = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='sell_record')
    date = models.DateTimeField(auto_now=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='sell_record')
    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='sell_record')
