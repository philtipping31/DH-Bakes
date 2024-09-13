from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonial(models.Model):
    """ A model representing a single testimonial in the database """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, blank=True, null=True)
    testimonial_text = models.TextField(max_length=1000, blank=True)
    rating = models.PositiveIntegerField(default=5, help_text="Rating between 1 and 5")
    date_submitted = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_submitted']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f'{self.name} - {self.title}'