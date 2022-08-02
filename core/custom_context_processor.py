from django.db.models import Count
from cart.models import Cart

def get_cart(request):
    cart = Cart.objects.get(pk=request.session['cart_id'])
    total_of_items = cart.products.aggregate(Count('name'))['name__count'] or 0
    
    return {
        'total_of_items': total_of_items
    }