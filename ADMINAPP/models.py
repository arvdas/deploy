from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
 
    description = models.TextField()

class Product(models.Model):
    productName = models.CharField(max_length=15)
    productDescription = models.TextField()
    productPrice=models.IntegerField()
    productImage = models.ImageField(upload_to='PRODUCT_IMAGE',default='null.jpg')
    category = models.CharField(max_length=100,default='0')
    stock = models.IntegerField()