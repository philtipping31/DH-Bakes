from django.db import models

class Recipe(models.Model):
    """ 
    A model representing an individual recipe in the database.
    """
    
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    prep_time = models.PositiveIntegerField(blank=True, null=True, help_text="Preparation time in minutes")
    cook_time = models.PositiveIntegerField(blank=True, null=True, help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField(blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']  # Order by newest recipes first
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title

    def total_time(self):
        return self.prep_time + self.cook_time

