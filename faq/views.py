from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import FAQCategory, FAQ

def faq_list(request):
    """
    Display a list of FAQs grouped by category.
    """
    categories = FAQCategory.objects.prefetch_related('faq_set').all()
    context = {
        'categories': categories,
    }
    return render(request, 'faq/faq_list.html', context)