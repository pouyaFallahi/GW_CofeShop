from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.apps import apps
from django.utils.html import mark_safe


# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, phone=None, email=None, password=None, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, phone, email, password, **extra_fields)

    def create_superuser(self, username, phone=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, phone, email, password, **extra_fields)


class MyUser(AbstractUser):
    differentـgender = [
        ("F", "زن"),
        ("M", "مرد"),
        ("o", "متفرقه"),
    ]
    roles = [("A", "Accountant"), ("B", "Barista"), ("C", "Cashier"), ("S", " Server")]
    role = models.CharField(max_length=1, choices=roles)
    phone = models.CharField(max_length=12, null=True)
    gender = models.CharField(max_length=1, choices=differentـgender)
    address = models.TextField()
    password = models.CharField(blank=False, null=False, max_length=50)
    is_manager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}'

def get_default_image():
    return "images/default/default.jpeg"

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(verbose_name='CategoryImage', upload_to='images/user_uploads', null=True, blank=True,
                              default=get_default_image)


    def __str__(self):
        return f'{self.name}'

class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=100)
    price = models.FloatField()

    image = models.ImageField(verbose_name='ItemImage', upload_to='images/user_uploads', null=True, blank=True, default=get_default_image)

    def __str__(self):
        return f'{self.name}'
    def image_preview(self):
         return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.image))
    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src= "{}" width="200" height="200" />' .format(self.image.url))


class CustomerOrder(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='customer_orders')
    item = models.ManyToManyField(
        Item, related_name="customer_orders")
    item_quantity = models.IntegerField()
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'


class SellRecord(models.Model):
    order = models.ForeignKey(
        CustomerOrder, on_delete=models.CASCADE, related_name="sell_records")
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="sell_records")
    date = models.DateField()

    def __str__(self):
        return f'{self.date}'


class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    level_rate = (
        (5, 'عالی'),
        (4, 'خیلی خوب'),
        (3, 'خوب'),
        (2, 'متوسط'),
        (1, 'افتضاح...')
    )

    rate = models.IntegerField(default=3, choices=level_rate)

    def __str__(self):
        return f'{self.user}'
