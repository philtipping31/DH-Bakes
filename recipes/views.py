from django.shortcuts import render, reverse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Recipe


def recipe_list(request):
    """View to display a list of approved recipes"""

    query = request.GET.get('q', None)
    recipes = Recipe.objects.filter(is_approved=True).order_by('-date_posted')

    # Apply search filtering
    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(ingredients__icontains=query)
        )

    # Paginate the recipes (1 recipe per page)
    paginator = Paginator(recipes, 1)  # Show 1 recipe per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'recipes/recipe_list.html'
    context = {
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }

    return render(request, template, context)
