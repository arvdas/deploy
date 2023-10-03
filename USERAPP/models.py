from django.db import models

from ADMINAPP.models import Product

# Create your models here.
class Customer(models.Model):
    FName = models.CharField(max_length=15)
    LName = models.CharField(max_length=15)
    Email = models.EmailField()
    Message = models.TextField()

class Register(models.Model):
    Username = models.CharField(max_length=15, default='')
    Phone_no = models.CharField(max_length=10, default='')
    Email = models.EmailField()
    Password = models.CharField(max_length=8)

class Cart(models.Model):
    userid = models.ForeignKey(Register, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.IntegerField()
    status = models.IntegerField(default=0)

class Booking(models.Model):
    userid = models.ForeignKey(Register, on_delete=models.CASCADE)
    cartid = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
    status = models.IntegerField(default=0)
   
    Address = models.CharField(max_length=255, default='')
    City = models.CharField(max_length=15, default='')
    State = models.CharField(max_length=15, default='')

class Complaint(models.Model):
    userid = models.ForeignKey(Register, on_delete=models.CASCADE)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=255)


 

   
