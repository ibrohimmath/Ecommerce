from django.db import models

from shop.models import Category, Product

class Order(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField() 
    address = models.CharField(max_length = 200)
    postal_code = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    paid = models.BooleanField(default = False)

    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name = 'items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name = 'orderitems', on_delete = models.CASCADE)
    
    quantity = models.PositiveIntegerField(default = 1)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)


    class Meta:
        verbose_name = 'orderitem'
        verbose_name_plural = 'orderitems'

    def get_cost(self):
        return self.quantity * self.price