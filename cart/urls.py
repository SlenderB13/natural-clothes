from xml.etree.ElementInclude import include
from django.urls import path 
from .views import add_product, remove_product, bag, avaliate

app_name = 'cart'
urlpatterns = [
    path('add_product/<int:id>', add_product, name='add_product'),
    path('remove_product/<int:id>', remove_product, name='remove_product'),
    path('bag/', bag, name='bag'),
    path('avaliate/', avaliate, name='avaliate'),
]
#o ideal seria products/add/id