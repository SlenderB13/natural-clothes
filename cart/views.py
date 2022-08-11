from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum

from cart.models import Cart, Product

def add(request, id):
    cart = Cart.objects.get(pk = request.session['cart_id'])

    product = get_object_or_404(Product, pk=id)
    cart.products.add(product)

    return redirect('home')

def remove(request, id):
    cart = Cart.objects.get(pk = request.session['cart_id'])

    product = get_object_or_404(Product, pk=id)
    cart.products.remove(product)

    return redirect('cart:bag')

def bag(request):
    cart = Cart.objects.get(pk = request.session['cart_id'])

    products = cart.products.all()
    total = products.aggregate(Sum('price'))['price__sum'] or 0.0

    return render(request, 'cart/cart.html', context={'products': products, 'total': total})

def avaliate(request):
    return render(request, 'cart/avaliation.html')

def payment(request):
    return render(request, 'cart/payment.html')

def success(request):
    cart = Cart.objects.get(pk = request.session['cart_id'])

    products = cart.products.clear()

    return render(request, 'cart/success.html')