import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, phone, email=None, password=None):
        if not phone:
            raise ValueError("The Phone Number is required")

        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email)
        user.set_password(password)
        user.save()  # using=self._db
        return user

    def create_superuser(self, phone, email=None, password=None):
        user = self.create_user(phone, email=None, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()  # using=self._db
        return user


def validate_phone_number(value):
    if not re.match(r'^\+?\d(8, 15)$', value):
        raise ValidationError('Invalid Phone Number')


class CustomUser(PermissionsMixin, AbstractBaseUser):
    GENDER_CHOICES = [
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('OTHER', 'Other'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(blank=False, null=False, unique=True, max_length=100)
    password = models.CharField(blank=False, null=False, max_length=50)
    phone = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, null=True, blank=True, validators=[validate_email])

    is_customer = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        # abstract = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class CustomerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_customer=True)


# Customer.customers.filter(name__icontain='')
class Customer(CustomUser):
    customers = CustomerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_customer = True
        super().save(*args, **kwargs)


class StaffManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is__staff=True)


class Staff(CustomUser):
    staffs = StaffManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)


class ManagerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_manager=True)


class Manager(CustomUser):
    managers = ManagerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_manager = True
        super().save(*args, **kwargs)
