from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User


# Create your models here.
class Product(models.Model):
    product = models.CharField(max_length=32)
    adder = models.ForeignKey(User, related_name="added_products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    wisher = models.ForeignKey(User, related_name="wishlist")
    wishitem = models.ForeignKey(Product, related_name="wishlists")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
