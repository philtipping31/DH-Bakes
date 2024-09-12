from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'title', 'testimonial_text', 'rating']

        RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
        widgets = {'rating': forms.Select(choices=RATING_CHOICES)}

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        # Set all fields as required
        for field in self.fields.values():
            field.required = True