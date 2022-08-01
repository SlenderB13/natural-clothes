from unittest.util import _MAX_LENGTH
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    image = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name