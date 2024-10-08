from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products,
    including sorting products and performing search queries
    """

    query = request.GET.get('q', None)
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        # Filter products based on the query
        products = products.filter(queries)
    elif query == '':
        messages.error(request,
                       "You did not submit any recognised search criteria")
        return redirect(reverse('products'))  # Redirect if the query is empty

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show a specific product in detail """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store"""
    products = Product.objects.all()

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request,
                             'Successfully added product to the store')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product.'
                           'Please check the from before submitting again')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
        'products': products,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in DH Bakes store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do this')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product successfully.'
                           'Please check the from before resubmitting.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are now editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """A view to handle deleting an existing product"""

    product = get_object_or_404(Product, pk=product_id)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product.delete()
        messages.success(request, "Successfully deleted product")
        return redirect('add_product')

    template = 'products/delete_product.html'
    context = {'product': product}
    return render(request, template, context)
