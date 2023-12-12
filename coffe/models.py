from django.db import models

# Create your models here.
class User(models.Model):
    differentـgender = {
        "F": "Female",
        "M": "Male",
        "o": "other"}
    roles={"B":"Barista","C":"Cashier","A":"Accountant","S":" Server"}
    role = models.CharField(max_length=1,choices=roles)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    gender = models.CharField(max_length=1,choices=differentـgender)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images/user/")
    username = models.CharField(
        blank=False, null=False, unique=True, max_length=100)
    password = models.CharField(blank=False, null=False, max_length=50)
    is_manager=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    category= models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image=models.ImageField(upload_to="images/item/")


    def __str__(self):
        return f'{self.name}'


class CustomerOrder(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer_orders')
    item = models.ManyToManyField(
        Item, related_name="customer_orders")
    item_quantity = models.IntegerField()
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name}-{self.user.last_name}'


class SellRecord(models.Model):
    order= models.ForeignKey(
        CustomerOrder, on_delete=models.CASCADE, related_name="sell_records")
    user= models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sell_records")
    date = models.DateField()

    def __str__(self):
        return f'{self.date}'
class Comment(models.Model):
    item=models.ForeignKey(Item,on_delete=models.CASCADE,related_name="comments")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    content=models.TextField()
    level_rate= (
    (5, 'عالی'),
    (4, 'خیلی خوب'),
    (3, 'خوب'),
    (2, 'متوسط'),
    (1, 'افتضاح...')
    )

    rate=models.IntegerField(default=3,choices=level_rate)
    def __str__(self):
        return f'{self.user.first_name}-{self.user.last_name}'