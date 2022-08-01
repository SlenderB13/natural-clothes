from django.urls import path 
from .views import add_product, remove_product, bag

urlpatterns = [
    path('add_product/<int:id>', add_product, name='add_product'),
    path('remove_product/<int:id>', remove_product, name='remove_product'),
    path('bag', bag, name='bag'),
]