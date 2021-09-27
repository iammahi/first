

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import jsonfield 

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    

class Types(models.Model):
    name = models.ForeignKey(Items,null=True ,on_delete=models.CASCADE)
    types = models.CharField(max_length=200, null=True)
    img  = models.ImageField(upload_to='images',null=True)
    price = models.FloatField(null=True)
    dicr   = models.TextField(null=True)
    def __str__(self):
        return self.types
class Jobs(models.Model):
    designation = models.CharField(max_length=200,null=True)
    img         = models.ImageField(upload_to='images',null=True)
    name        = models.CharField(max_length=200,null=True)
    decr        = models.TextField(null=True)
    #link = models.URLField(null=True)
    #icon = models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.designation
    
class Address(models.Model):
    address = models.TextField(null=True)
    ph_no =models.PositiveIntegerField(null=True)
    email = models.EmailField(null=True)





class ConForm_Orders(models.Model):
    status_list = [('Order not packed','Order not packed'),('Ready to Dlivery','Ready to Dlivery'),('Order Deliveried','Order Deliveried')]
    price = models.FloatField()
    balance  = models.FloatField(null=True)
    time  = models.TimeField(auto_now_add=True,null=True)
    name  = models.CharField(null=True, max_length=50)
    email = models.EmailField()
    ph_no = models.PositiveIntegerField()
    addr  = models.TextField()  
    json =  jsonfield.JSONField(null=True)
    date  = models.DateField(auto_now_add=True)
    payment  = models.CharField( max_length=100)
    payment_mode  = models.CharField(null=True, max_length=50,default='Paid')
    advance  = models.FloatField(null=True,default=0)
    status    = models.CharField(choices=status_list,default='Order not packed', max_length=150)
    delivery_boy_id  = models.ForeignKey(User,on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.name