from django import forms 
from .cart import Cart
from shop.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = PRODUCT_QUANTITY_CHOICES, coerce = int, widget = forms.Select(attrs = {'style': 'margin-left: 7px; margin-right: 0; max-width: 45px;'}))
    override = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)