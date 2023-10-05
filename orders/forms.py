from django import forms 

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order 
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city'] 
        widgets = {
            'first_name': forms.TextInput(attrs = {'class': 'input-info'}),
            'last_name': forms.TextInput(attrs = {'class': 'input-info'}),
            'email': forms.EmailInput(attrs = {'class': 'input-info'}),
            'address': forms.TextInput(attrs = {'class': 'input-info'}),
            'postal_code': forms.TextInput(attrs = {'class': 'input-info'}),
            'city': forms.TextInput(attrs = {'class': 'input-info'}),
        }