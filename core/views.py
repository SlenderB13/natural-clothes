from django.shortcuts import render, get_object_or_404

from core.models import Product
from cart.models import Cart

def home(request):
    try:
        cart_id = request.session['cart_id']
    except:
        cart = Cart()
        cart.save()

        request.session['cart_id'] = cart.pk

    products = Product.objects.all()

    return render(request, 'core/home.html', context={'products': products})

def product(request, id):
    product = get_object_or_404(Product, pk=id)

    return render(request, 'core/product.html', context={'product': product})

# services.py para o criar o carrinho