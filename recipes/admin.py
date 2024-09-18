from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'ingredients',
                    'instructions', 'prep_time',
                    'cook_time', 'servings',
                    'image', 'is_approved')

    list_filter = ('is_approved', 'date_posted')

    ordering = ('-date_posted',)

    actions = ['approve_recipes']

    # Custom admin action to approve selected recipes
    def approve_recipes(self, request, queryset):
        queryset.update(is_approved=True)
    approve_recipes.short_description = 'Approve selected recipes'
