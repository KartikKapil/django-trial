from django.db import models

# Create your models here.
# created this customer model

class Customer(models.Model):
    name  = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY = (('Indoor','Indoor'),('Out Door','Out Door'))
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    # customer = 
    # product =
    STATUS = (('Pending','Pending'),('Out for Delivery','Out for Delivery'),('Delivered','Delivered'))
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    staus =  models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
        return self.name
    