from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from .forms import ContactForm

# Create your views here.

def contact(request):
    """
    Handle the contact form submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.created_at = timezone.now()
            contact.save()
            messages.success(request, "Thank you! Your enquiry has been submitted successfully.")
            form = ContactForm()
        else:
            messages.error(request, "There was an error with your submission. Please check your details.")
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)