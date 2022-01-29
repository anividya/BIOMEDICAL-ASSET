from django.db.models import fields
from django.forms.widgets import DateTimeInput
import django_filters
from django_filters import DateFromToRangeFilter

from .models import *

class AssetFilter(django_filters.FilterSet):

    assetname = django_filters.CharFilter(field_name = 'assetname', lookup_expr='iexact')
    Make = django_filters.CharFilter(field_name = 'asset_make', lookup_expr='iexact')
    Model = django_filters.CharFilter(field_name = 'asset_model', lookup_expr='icontains')
    Dept = django_filters.CharFilter(field_name = 'dept', lookup_expr='icontains')
    pmstat = django_filters.CharFilter(field_name = 'pmstat', lookup_expr='icontains')
    pmdue = django_filters.NumberFilter(field_name='pmdue', lookup_expr='month')
    pmduerange = django_filters.DateTimeFromToRangeFilter(field_name='pmdue' )
    
    class Meta:
        models = Asset

class CalFilter(django_filters.FilterSet):

    assetname = django_filters.CharFilter(field_name = 'assetname', lookup_expr='icontains')
    Make = django_filters.CharFilter(field_name = 'asset_make', lookup_expr='iexact')
    Model = django_filters.CharFilter(field_name = 'asset_model', lookup_expr='icontains')
    Dept = django_filters.CharFilter(field_name = 'dept', lookup_expr='icontains')
    calstat = django_filters.CharFilter(field_name = 'calstat', lookup_expr='icontains')
    caldue = django_filters.NumberFilter(field_name='caldue', lookup_expr='month')
    calduerange = django_filters.DateTimeFromToRangeFilter(field_name='caldue' )
    
    class Meta:
        models = Asset

class NmFilter(django_filters.FilterSet):

    assetname = django_filters.CharFilter(field_name = 'assetname', lookup_expr='icontains')
    make = django_filters.CharFilter(field_name = 'assetname', lookup_expr='icontains')
    
    
    class Meta:
        models = Asset
        

