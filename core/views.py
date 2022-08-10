from django.shortcuts import render, get_object_or_404

from .services import create_cart

from core.models import Product
from cart.models import Cart

def home(request):
    create_cart(request)

    products = Product.objects.all()

    return render(request, 'core/home.html', context={'products': products})

def product(request, id):
    product = get_object_or_404(Product, pk=id)

    return render(request, 'core/product.html', context={'product': product})

# services.py para o criar o carrinho