from django import forms
from django.forms import inlineformset_factory

from .models import Client, Contact


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'gender']
        widgets = {
            'gender': forms.Select()
        }


class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['value', 'kind', 'primary']
        widgets = {
            'value': forms.TextInput(),
            'kind': forms.Select(),
            'ptimary': forms.CheckboxInput(),
        }

ContactFormSet = inlineformset_factory(Client, Contact, form=AddContactForm, extra=1, can_delete=False)
