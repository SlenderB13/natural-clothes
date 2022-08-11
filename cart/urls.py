from xml.etree.ElementInclude import include
from django.urls import path 
from .views import bag, avaliate, payment, success

app_name = 'cart'
urlpatterns = [
    path('', bag, name='bag'),
    path('payment/', payment, name='payment'),
    path('avaliate/', avaliate, name='avaliate'),
    path('success/', success, name='success'),
]