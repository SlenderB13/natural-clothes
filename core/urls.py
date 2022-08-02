from distutils import core
from django.urls import path, include
from .views import home, product

urlpatterns = [
    path('', home, name='home'),
    path('cart/', include('cart.urls')),
    path('product/<int:id>', product, name='product'),
]
