from django import forms
from localflavor.pl.forms import PLPostalCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
    postal_code = PLPostalCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']