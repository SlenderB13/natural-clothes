from django.urls import path 
from .views import add_product, bag

urlpatterns = [
    path('add_product/<int:id>', add_product, name='add_product'),
    path('bag', bag, name='bag'),
]