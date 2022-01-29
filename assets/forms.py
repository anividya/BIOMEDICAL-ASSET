from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import widgets
from .models import Asset
from django.forms import ModelForm
from datetime import datetime, date

class DateInput(forms.DateInput):
    input_type = 'date'

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('assetid','assetname','asset_make','asset_model','slno','dept','pmdone','pmdue','caldone','caldue','wrstart','wrend','mcstart','mcend','stat')

        widgets = {
            'pmdue': DateInput(),
            'caldue' : DateInput(),
            'pmdone' : DateInput(),
            'caldone' : DateInput(),
            'wrstart' : DateInput(),
            'wrend' : DateInput(),
            'mcstart' : DateInput(),
            'mcend' : DateInput(),
        }
    def __init__(self, *arg, **kwargs):
        super(AssetForm,self).__init__(*arg, **kwargs)
