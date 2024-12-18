from django.db import models
from products.models import Product
# Create your models here.

from django.urls import reverse

class Cart(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def __str__(self):
        return self.cart_id
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveBigIntegerField(default=1)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product