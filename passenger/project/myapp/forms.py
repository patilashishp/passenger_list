from django.core import validators
from django import forms
from .models import *

class Passengerreg(forms.ModelForm):
    class Meta:
        model = passenger
        fields = ['name','age','gender','boarding','destination']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'boarding': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
        }
