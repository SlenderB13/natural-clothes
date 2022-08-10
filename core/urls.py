from distutils import core
from django.urls import path, include
from .views import home, products

urlpatterns = [
    path('', home, name='home'),
    path('cart/', include('cart.urls')),
    path('products/<int:id>', products, name='products'),
]
