__author__ = 'Arpit Gang'
from django import forms
#from django.forms import ModelForm
from .models import fill, show


class dataForm(forms.ModelForm):
    class Meta:
        model = fill
        fields = ['Full_name', 'Add', 'ipadd', 'phoneno']
