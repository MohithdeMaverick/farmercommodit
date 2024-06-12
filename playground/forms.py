# farmers/forms.py

from django import forms
from .models import Farmer

class FarmerRegisterForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'crop_type', 'quantity', 'price_expectation', 'contact_no']
