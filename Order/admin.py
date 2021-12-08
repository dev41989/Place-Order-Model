from django.contrib import admin
from .models import order, OrderItem, Product

admin.site.register(order)
admin.site.register(OrderItem)
admin.site.register(Product)