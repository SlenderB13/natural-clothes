from cart.models import Cart


def create_cart(request):
    try:
        cart_id = request.session['cart_id']
    except:
        cart = Cart()
        cart.save()

        request.session['cart_id'] = cart.pk