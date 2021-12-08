from django.shortcuts import render
from .models import order, Product, OrderItem

# Create your views here.
def ordera(request):
    context = {
      'ProductList': Product.objects.all()
   }
    return render(request,'order.html',context = context)

def record(request):
    orders = order()
    OrderItems = OrderItem()
    products = Product()
    
    orders.Firstname = request.POST['First name']
    orders.Lastname = request.POST['Last name']
    orders.Email = request.POST['Email']
    orders.Address_street = request.POST['Street']
    orders.Address_landmark = request.POST['Landmark']
    orders.Address_pincode = request.POST['Postal Code']
    OrderItems.Quantity = request.POST['Quantity']
    OrderItems.price = request.POST['Price']
    data = request.POST['Data']
    data1 = Product.objects.get(name = data)

    OrderItems.product = data1    
    orders.save()
    OrderItems.order = order.objects.last()
    OrderItems.save()
    return render(request,'success.html')

def Show_data(request):
    context = {
      'orderdata': OrderItem.objects.all()
    }
    return render(request,'record.html',context = context)

def deletedata(request,delete_id):
    object = OrderItem.objects.get(id = delete_id)
    object.delete()
    context = {
      'orderdata': OrderItem.objects.all()
    }
    return render(request,'record2.html',context = context)    


def Modify_show(request,show_id):
    context = {
        #object : OrderItem.objects.get(id = show_id)
        'Moddata': OrderItem.objects.get(id = show_id),
        'ProductList': Product.objects.all()
    }
    return render(request,'Order_edit.html',context = context)

def Edit_Modify(request):
    id = request.POST['id']
    updaterecord = OrderItem.objects.get(id = id)
    updaterecord.order.Firstname = request.POST['First name']
  
    updaterecord.order.Lastname = request.POST['Last name']
    updaterecord.order.Email = request.POST['Email']
    updaterecord.order.Address_street = request.POST['Street']
    updaterecord.order.Address_landmark = request.POST['Landmark']
    updaterecord.order.Address_pincode = request.POST['Postal Code']
    updaterecord.Quantity = request.POST['Quantity']
    updaterecord.price = request.POST['Price']
    updaterecord.order.save()
    updaterecord.save()

    context = {
      'orderdata': OrderItem.objects.all()
    }
    return render(request,'record.html',context = context)
    
