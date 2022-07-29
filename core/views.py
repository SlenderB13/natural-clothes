from django.shortcuts import render

from core.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', context={'products': products})

def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'core/product.html', context={'product': product})