from django.shortcuts import render
from .models import Testimonial


# Create your views here.

def testimonial_list(request):
    """ A View to display all approved testimonials"""
    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-date_submitted')

    template = 'testimonials/testimonial_list.html'
    context = {
        'testimonials': testimonials
    }
    return render(request, template, context)