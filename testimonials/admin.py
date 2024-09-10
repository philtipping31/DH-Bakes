from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'rating', 'date_submitted', 'is_approved')
    list_filter = ('is_approved', 'date_submitted')
    search_fields = ('name', 'title', 'testimonial_text')
    ordering = ('-date_submitted',)
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(is_approved=True)
    approve_testimonials.short_description = 'Mark selected testimonials as approved'
