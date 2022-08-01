from django.shortcuts import render

from cart.models import Cart, Product

cart = Cart()
cart.save()

def add_product(request, id):
    cart.products.add(Product.objects.get(id=id))
    return render(request, 'core/home.html')