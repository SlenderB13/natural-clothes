from django.db import models
from core.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True, null=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return str(self.pk)