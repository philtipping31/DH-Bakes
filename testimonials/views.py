from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Testimonial
from .forms import TestimonialForm


def testimonial_list(request):
    """ A View to display all approved testimonials"""
    testimonials = Testimonial.objects.filter(
        is_approved=True
    ).order_by('-date_submitted')

    template = 'testimonials/testimonial_list.html'
    context = {
        'testimonials': testimonials
    }
    return render(request, template, context)


@login_required
def add_testimonial(request):
    """A view to handle adding a new testimonial - new testimonials
    will be shown in admin only until approved."""

    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.is_approved = False
            testimonial.save()
            messages.success(request,
                             'Testimonial submitted and awaiting approval!'
                             'Thank you.')
            return redirect('testimonial_list')
    else:
        form = TestimonialForm()

    template = 'testimonials/add_testimonial.html'
    context = {'form': form}
    return render(request, template, context)


def edit_testimonial(request, testimonial_id):
    """A view to handle editing an existing testimonial.
    Edited testimonial will go back to waiting approval after submitting."""

    testimonial = get_object_or_404(Testimonial, id=testimonial_id)

    if testimonial.user != request.user:
        messages.error(request,
                       "You are not allowed to edit this testimonial.")
        return HttpResponseForbidden(render(request, '403.html'))

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.is_approved = False
            testimonial.save()

            messages.success(request, "Your testimonial was updated!"
                             "We need to approve this again before showing"
                             "it on our site. Thank you!")
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)

    template = 'testimonials/edit_testimonial.html'
    context = {'form': form, 'testimonial': testimonial}
    return render(request, template, context)


def delete_testimonial(request, testimonial_id):
    """A view to handle deleting an existing testimonial"""

    testimonial = get_object_or_404(Testimonial, id=testimonial_id)

    if testimonial.user != request.user:
        messages.error(request,
                       "You are not allowed to delete this testimonial.")
        return HttpResponseForbidden(render(request, '403.html'))

    if request.method == 'POST':
        testimonial.delete()
        messages.success(request, "Successfully deleted testimonial")
        return redirect('testimonial_list')

    template = 'testimonials/delete_testimonial.html'
    context = {'testimonial': testimonial}
    return render(request, template, context)
