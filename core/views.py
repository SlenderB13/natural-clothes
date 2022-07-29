from django.shortcuts import render

from core.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html', context={'products': products})