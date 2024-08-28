import uuid
from django.db import models
from django.conf import settings
from products.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=32, editable=False)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=40)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    town_or_city = models.CharField(max_length=40)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True, null=True)
    county = models.CharField(max_length=80, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID."""
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.delivery_cost = self.order_total + settings.STANDARD_DELIVERY
        
        self.grand_total = self.order_total + self.delivery_cost
        self.save()


    def save(self, *args, **kwargs):
        """Override the save method to set the order number if not set."""
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        """Override the save method to calculate the line item total and update the order total."""
        self.lineitem_total = self.product.price * self.quantity
        super(OrderLineItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'