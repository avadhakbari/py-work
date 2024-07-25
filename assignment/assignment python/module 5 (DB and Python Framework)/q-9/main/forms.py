from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product', 'product_price', 'image', 'product_model', 'product_ram')