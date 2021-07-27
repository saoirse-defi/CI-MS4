from django import forms
from .models import Seller


class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        widgets = {'password': forms.PasswordInput()}
        fields = ['username', 'email', 'town', 'county', 'password']

