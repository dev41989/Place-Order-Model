from django.db import models
from datetime import datetime

class order(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Email = models.EmailField()
    Address_street = models.TextField()
    Address_landmark = models.TextField()
    Address_pincode = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100,unique = True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(order, on_delete = models.CASCADE)
    Quantity = models.IntegerField()
    price = models.IntegerField()

    def get_absolute_url(self):
        return reverse('work_orders:detail', kwargs={'delete_id': self.id})

    def get_absolute_url(self):
        return reverse('work_orders:detail', kwargs={'show_id': self.id})  

    def get_absolute_url(self):
        return reverse('work_orders:detail', kwargs={'edit_id': self.id})      
    


# Create your models here.
