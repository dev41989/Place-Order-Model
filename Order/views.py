from django.shortcuts import render
from .models import Order, Product, OrderItem

# Create your views here.
#Show Order Page
def base_order_function(request):
    context = {
      'ProductList': Product.objects.all()
   }
    return render(request,'order.html',context = context)

def record_order_function(request):
    orders = Order()
    OrderItems = OrderItem()
    products = Product()
    
    orders.firstname = request.POST['first_name']
    orders.lastname = request.POST['last_name']
    orders.email = request.POST['email']
    orders.address_street = request.POST['street']
    orders.address_landmark = request.POST['landmark']
    orders.address_pincode = request.POST['postal_code']
    OrderItems.quantity = request.POST['quantity']
    OrderItems.price = request.POST['price']
    
    product_data = request.POST['data']
    product_data1 = Product.objects.get(name = product_data)
    OrderItems.product = product_data1    
    
    orders.save()
    
    OrderItems.order = Order.objects.last()
    OrderItems.save()

    return render(request,'success.html')

def show_data_function(request):
    context = {
      'orderdata': OrderItem.objects.all()
    }
    return render(request,'record.html',context = context)

def delete_data_function(request,delete_id):
    object = OrderItem.objects.get(id = delete_id)
    object.delete()
    context = {
      'orderdata': OrderItem.objects.all()
    }
    return render(request,'record2.html',context = context)    


def modify_show_function(request,show_id):
    context = {
        #object : OrderItem.objects.get(id = show_id)
        'modify_data': OrderItem.objects.get(id = show_id),
        'productList': Product.objects.all()
    }
    return render(request,'Order_edit.html',context = context)

def edit_Modify_function(request):
    id = request.POST['id']
    update_record = OrderItem.objects.get(id = id)
    update_record.order.firstname = request.POST['first_name']
  
    update_record.order.lastname = request.POST['last_name']
    update_record.order.email = request.POST['email']
    update_record.order.address_street = request.POST['street']
    update_record.order.address_landmark = request.POST['landmark']
    update_record.order.address_pincode = request.POST['postal_code']
    update_record.quantity = request.POST['quantity']
    update_record.price = request.POST['price']
    update_record.order.save()
    update_record.save()

    context = {
      'orderdata': OrderItem.objects.all()
    }
    return render(request,'record.html',context = context)
    
