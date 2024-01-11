from django import forms
from models import *

class AddClient(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    gender = forms.CharField(max_length=1)
    contact = forms.CharField(max_length=160)
    primary = forms.BooleanField()
