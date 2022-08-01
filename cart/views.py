from django.shortcuts import render

from cart.models import Cart, Product

cart = Cart()
cart.save()

def add_product(request, id):
    cart.products.add(Product.objects.get(id=id))
    return render(request, 'core/home.html')

def bag(request):
    products = cart.products.all()
    return render(request, 'cart/cart.html', context={'products': products})