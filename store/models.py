from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, default="")
    thumbnail = models.ImageField(upload_to='product', null=True, blank=True)

