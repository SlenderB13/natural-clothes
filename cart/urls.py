from xml.etree.ElementInclude import include
from django.urls import path 
from .views import bag, avaliate, payment

app_name = 'cart'
urlpatterns = [
    path('', bag, name='bag'),
    path('payment/', payment, name='payment'),
    path('avaliate/', avaliate, name='avaliate'),
]
#o ideal seria products/add/id