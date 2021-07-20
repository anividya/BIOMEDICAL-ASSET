from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from .models import Asset
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'
        widgets = {
            'pmdue': DateInput(),
            'caldue' : DateInput(),
            'pmdone' : DateInput(),
            'caldone' : DateInput(),
        }
    def __init__(self, *arg, **kwargs):
        super(AssetForm,self).__init__(*arg, **kwargs)
