from django import forms
from .models import Client


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'gender']
        widgets = {
            'gender': forms.Select()
        }
