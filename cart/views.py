from django.shortcuts import get_object_or_404, render
from django.db.models import Sum

from cart.models import Cart, Product

cart = Cart()
cart.save()

def add_product(request, id):
    cart.products.add(Product.objects.get(id=id))
    return render(request, 'cart/cart.html')

def remove_product(request, id):
    product = get_object_or_404(Product, pk=id)
    cart.products.remove(product)
    return render(request, 'cart/cart.html')

def bag(request):
    products = cart.products.all()
    total = products.aggregate(Sum('price'))['price__sum'] or 0.0
    return render(request, 'cart/cart.html', context={'products': products, 'total': total})