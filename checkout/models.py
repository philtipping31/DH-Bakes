from decimal import Decimal

import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    """
    A model representing a customer's order, which includes details
    like the customer's personal information, order total, delivery costs,
    and order-specific details like the unique order number, payment ID"""

    order_number = models.CharField(max_length=32, editable=False)
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='orders')
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True, null=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2, default=0)
    order_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10,
                                      decimal_places=2, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254,
                                  null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID.
        """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = (
            self.lineitems.aggregate(Sum('lineitem_total'))
            .get('lineitem_total__sum') or 0
        )
        self.delivery_cost = Decimal(settings.STANDARD_DELIVERY)
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the save method to set the order number if not set.
        """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    A model representing a single line item within an order.
    Each line item is associated with a specific product and includes
    information about the quantity ordered and
    the total price for that line item.
    """

    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """Override the save method to calculate the line item total
        and update the order total."""
        self.lineitem_total = self.product.price * self.quantity
        super(OrderLineItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
