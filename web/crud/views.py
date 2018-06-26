from django.shortcuts import render, redirect
from .models import Category, Product, Order, DeliveryType
from django.contrib.auth.models import User
import os, json, logging, datetime, shutil, zipfile
logger = logging.getLogger(__name__)

def showProduct(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    logger.error(products)
    context = {'products': products, 'categories' : categories}
    return render(request, 'product/index.html', context)

def createProduct(request):
    category = Category.objects.get(id=request.POST['category'])
    logger.error(category)
    product = Product(image=request.POST['image'], title=request.POST['title'], description = request.POST['description'],
    price = request.POST['price'], currency = request.POST['currency'], category = category)
    product.save()
    return redirect('/7ninja/product')

def editProduct(request, id):
    products = Product.objects.get(id=id)
    categories = Category.objects.all()
    context = {'products': products,'categories' : categories}
    return render(request, 'product/edit.html', context)

def updateProduct(request, id):    
    product = Product.objects.get(id=id)
    product.image = request.POST['image']
    product.title = request.POST['title']
    product.description = request.POST['description']
    product.price = request.POST['price']
    product.currency = request.POST['currency']

    category = Category.objects.get(id=request.POST['category'])
    product.category = category

    product.save()
    return redirect('/7ninja/product')

def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/7ninja/product')

def showOrder(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    users = User.objects.all()
    deliveries = DeliveryType.objects.all()
    context = {'orders': orders, 'deliveries':deliveries, 'users': users, 'products':products}
    return render(request, 'order/index.html', context)

def createOrder(request):
    product = Product.objects.get(id=request.POST['product'])
    user = User.objects.get(id=request.POST['user'])
    delivery = DeliveryType.objects.get(id=request.POST['delivery'])
    product_count = int(request.POST['product_count'])

    product_price = int(product.price)
    delivery_price = int(delivery.price)

    if delivery.fixed == 'TRUE':
        total_price = product_price*product_count + delivery_price
    else:
        total_price = product_price*product_count+ (product_price*product_count*delivery_price/100)

    logger.error(product_price)
    logger.error(delivery_price)
    logger.error(total_price)

    order = Order(product=product, user=user, delivery= delivery, product_count = product_count, total_price = total_price)
    order.save()
    return redirect('/7ninja/order')

def editOrder(request, id):
    orders = Order.objects.get(id=id)
    context = {'orders': orders}
    return render(request, 'order/edit.html', context)

def updateOrder(request, id):   
    product = Product.objects.get(id=request.POST['product'])
    user = User.objects.get(id=request.POST['user'])
    delivery = DeliveryType.objects.get(id=request.POST['delivery'])
    product_count = request.POST['product_count'] 
    order = Order.objects.get(id=id)
    order.product = product
    order.user = user
    order.delivery = delivery
    order.product_count = product_count

    product_price = int(product.price)
    delivery_price = int(delivery.price)

    if delivery.fixed == 'TRUE':
        total_price = product_price + delivery_price
    else:
        total_price = product_price + (product_price*delivery_price/100)

    order.total_price = total_price
    order.save()
    return redirect('/7ninja/order')

def deleteOrder(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('/7ninja/order')

def showUser(request):
    members = User.objects.all()
    context = {'members': members}
    return render(request, 'user/index.html', context)

def createUser(request):
    # member = User(first_name=request.POST['firstname'], last_name=request.POST['lastname'], email = request.POST['email'], username = request.POST['username'], password=request.POST['password'])
    # member.save()

    user = User.objects.create_user(first_name=request.POST['firstname'], last_name=request.POST['lastname'], email = request.POST['email'], username = request.POST['username'], password=request.POST['password'])
    return redirect('/7ninja/user')

def editUser(request, id):
    members = User.objects.get(id=id)
    context = {'members': members}
    return render(request, 'user/edit.html', context)

def updateUser(request, id):    
    member = User.objects.get(id=id)
    member.first_name = request.POST['firstname']
    member.last_name = request.POST['lastname']
    member.email = request.POST['email']
    member.username = request.POST['username']
    member.save()
    return redirect('/7ninja/user')

def deleteUser(request, id):
    member = User.objects.get(id=id)
    member.delete()
    return redirect('/7ninja/user')

def showCategory(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'category/index.html', context)

def createCategory(request):
    category = Category(title=request.POST['title'])
    category.save()
    return redirect('/7ninja/category')

def editCategory(request, id):
    categories = Category.objects.get(id=id)
    context = {'categories': categories}
    return render(request, 'category/edit.html', context)

def updateCategory(request, id):    
    category = Category.objects.get(id=id)
    category.title = request.POST['title']
    category.save()
    return redirect('/7ninja/category')

def deleteCategory(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/7ninja/category')

def showDelivery(request):
    deliveryTypes = DeliveryType.objects.all()
    context = {'deliveryTypes': deliveryTypes}
    return render(request, 'delivery/index.html', context)

def createDelivery(request):
    deliveryType = DeliveryType(title=request.POST['title'], price = request.POST['price'], fixed= request.POST['fixed'])
    deliveryType.save()
    return redirect('/7ninja/delivery')

def editDelivery(request, id):
    deliveryTypes = DeliveryType.objects.get(id=id)
    context = {'deliveryTypes': deliveryTypes}
    return render(request, 'delivery/edit.html', context)

def updateDelivery(request, id):    
    deliveryType = DeliveryType.objects.get(id=id)
    deliveryType.title = request.POST['title']
    deliveryType.price = request.POST['price']
    deliveryType.fixed = request.POST['fixed']
    deliveryType.save()
    return redirect('/7ninja/delivery')

def deleteDelivery(request, id):
    deliveryType = DeliveryType.objects.get(id=id)
    deliveryType.delete()
    return redirect('/7ninja/delivery')