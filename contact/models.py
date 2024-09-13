from django.db import models
from django.utils import timezone


# Form of contact choices
SELECT_FORM_OF_CONTACT = (
    ("email", "E-mail"),
    ("phone", "Phone"),
)

# Question category choices
SELECT_QUESTION_CATEGORIES = (
    ("general_enquiry", "General Enquiry"),
    ("placed_order", "Placed Order"),
    ("delivery", "Delivery"),
    ("custom_bake_request", "Custom Bake Request"),
    ("special_events", "Special Events"),
    ("other", "Other"),
)

# Enquiry status choices
SELECT_ENQUIRY_STATUS = (
    ("new", "New"),
    ("pending", "Pending"),
    ("in_progress", "In Progress"),
    ("resolved", "Resolved"),
)

class Contact(models.Model):
    """
    A model representing a contact enquiry form submission.
    """
    name = models.CharField(max_length=100, verbose_name="Your Name")
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField( max_length=11, blank=True, verbose_name="Phone Number")
    subject = models.CharField(max_length=100, verbose_name="Subject",)
    form_of_contact = models.CharField(
        max_length=10,
        choices=SELECT_FORM_OF_CONTACT,
        default='email',
        verbose_name="Preferred Contact Method"
    )
    question_category = models.CharField(
        max_length=50,
        choices=SELECT_QUESTION_CATEGORIES,
        default='general_enquiry',
        verbose_name="Enquiry Type"
    )
    message = models.TextField(max_length=3000, verbose_name="Message Details")
    status = models.CharField(
        max_length=20,
        choices=SELECT_ENQUIRY_STATUS,
        default='new',
        verbose_name="Enquiry Status"
    )

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Submitted On")
    
    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Contact Enquiry"
        verbose_name_plural = "Contact Enquiries"
        ordering = ['-created_at']  # Newest first
