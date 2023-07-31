from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
#<-----Category Model------>

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name

#<-----Products Model------>

class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
    description = models.CharField(
        max_length=250,default='',blank=True,null=True
    )
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_byid(ids):
        return Products.objects.all()
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

#<-----Customer Model------>

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def register(self):
        self.save()
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user
    
class Purchase(models.Model):
    bookid = models.CharField(max_length=9)
    dtime = models.DateTimeField()
    name = models.CharField(max_length=30)
    mob = models.CharField(max_length=10)
    mail = models.EmailField()
    add1 = models.CharField(max_length=30)
    add2 = models.CharField(max_length=30)
    pin = models.CharField(max_length=6)
    items = models.TextField(max_length=500)
    opt = [
        ('cod','Cash On Delivery'),
        ('upi','UPI'),
        ('nb','Net Banking'),
    ]
    payment = models.CharField(max_length=30,choices=opt)
    amnt = models.CharField(max_length=6)

    def __str__(self):
        return self.bookid

