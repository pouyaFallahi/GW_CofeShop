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
    # customer_id = models.AutoField()

    def __str__(self):
        return f"{self.first_name} -{self.last_name}"


class Staff(User):
    # staff_id = models.AutoField()
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"


class Manager(User):
    # manager_id = models.AutoField()
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="managers"
        )

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"
    
# class CustomerOrder(models.Model):
#     customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_orders')
#     item=models.
