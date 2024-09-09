from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'form_of_contact', 'question_category', 'status', 'created_at')
    list_filter = ('form_of_contact', 'question_category', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'subject', 'form_of_contact', 'question_category', 'message', 'status')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

admin.site.register(Contact, ContactAdmin)
