from django.db import models
from core.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True, null=True)
    total = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.pk)