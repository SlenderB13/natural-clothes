from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum

from cart.models import Cart, Product

def add_product(request, id):
    cart = Cart.objects.get(pk = request.session['cart_id'])

    cart.products.add(Product.objects.get(id=id))

    return redirect('home')

def remove_product(request, id):
    cart = Cart.objects.get(pk = request.session['cart_id'])

    product = get_object_or_404(Product, pk=id)
    cart.products.remove(product)

    return redirect('home')
# voltar para o carrinho

def bag(request):
    cart = Cart.objects.get(pk = request.session['cart_id'])

    products = cart.products.all()
    total = products.aggregate(Sum('price'))['price__sum'] or 0.0

    return render(request, 'cart/cart.html', context={'products': products, 'total': total})