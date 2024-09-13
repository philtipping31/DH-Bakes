from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    A form for creating and updating `Product` instances.
    
    This form allows users to input all fields related to a product, 
    including an optional image, using the custom widget `CustomClearableFileInput`.
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black shadow-sm rounded-1'