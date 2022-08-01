from distutils import core
from django.urls import path
from .views import home, product

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:id>', product, name='product'),
]
