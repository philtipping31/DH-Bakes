from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    query = request.GET.get('q', None)  # Get the query parameter 'q', or None if it doesn't exist
    products = Product.objects.all()  

    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)  # Filter products based on the query
    elif query == '':
        messages.error(request, "You did not submit any recognised search criteria")
        return redirect(reverse('products'))  # Redirect if the query is empty

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show a specific product in detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)