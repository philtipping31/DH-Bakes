from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 
                  'subject', 'form_of_contact', 
                  'question_category', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Your Phone Number'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Your Subject Here'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Message Details'
            }),
        }