from django.contrib import admin
from .models import Asset


class AssetAdmin(admin.ModelAdmin):
    list_display = ('assetid','assetname','asset_make','asset_model','slno','dept','pmstat','calstat','stat')


# Register your models here.

admin.site.register(Asset,AssetAdmin)