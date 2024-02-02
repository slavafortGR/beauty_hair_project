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
        fields = ['contact', 'kind', 'primary']
        widgets = {
            'contact': forms.TextInput(),
            'kind': forms.Select(),
            'primary': forms.CheckboxInput(),
        }

ContactFormSet = inlineformset_factory(Client, Contact, form=AddContactForm, extra=1, can_delete=False)
