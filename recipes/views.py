from django.shortcuts import render
from .models import Recipe


def recipe_list(request):
    """View to display a list of approved recipes"""

    recipes = Recipe.objects.filter(is_approved=True).order_by('-date_posted')

    template = 'recipes/recipe_list.html'
    context = {
        'recipes': recipes
    }
    return render(request, template, context)
