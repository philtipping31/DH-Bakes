from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form':order_form,
        'stripe_public_key': 'pk_test_51PfJpk2MEDs47a1gzMsUUH0LR4xLU72WuBCuGJQSz7CyGvvl2ofnIM6IGBAitG7JNmTEmQKEQSB0soFKQhnnysuN008G2P9NRX',
        'client_secret': 'secret_key_test',
    }

    return render(request, template, context)