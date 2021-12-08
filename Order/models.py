from django.db import models
from datetime import datetime

class Order(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address_street = models.TextField()
    address_landmark = models.TextField()
    address_pincode = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100,unique = True)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def get_absolute_url(self):
        return reverse('work_orders:detail', kwargs={'delete_id': self.id})

    def get_absolute_url(self):
        return reverse('work_orders:detail', kwargs={'show_id': self.id})  

    def get_absolute_url(self):
        return reverse('work_orders:detail', kwargs={'edit_id': self.id})      
    


# Create your models here.
