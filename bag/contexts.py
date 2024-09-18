from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Retrieves the contents of the shopping bag from the session, calculates
    the total price, delivery costs, and product count, and returns these
    values in the context."""

    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    delivery = Decimal('0.00')

    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if product_count > 0:
        delivery = Decimal(settings.STANDARD_DELIVERY)

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
