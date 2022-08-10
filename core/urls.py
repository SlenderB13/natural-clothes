from distutils import core
from django.urls import path, include
from .views import home, products
from cart.views import add, remove

urlpatterns = [
    path('', home, name='home'),
    path('cart/', include('cart.urls')),
    path('products/<int:id>', products, name='products'),
    path('products/add/<int:id>', add, name='add'),
    path('products/remove/<int:id>', remove, name='remove'),
]
