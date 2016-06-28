from django.contrib import admin
from .models import *
from commons.admin import BaseAdmin


@admin.register(Asset)
class AssetAdmin(BaseAdmin):
    list_display = ['name','model','serial','show_spec','asset_group','asset_brand']
    exclude = ['createdby', 'modifiedby', 'deleted','image']
    list_per_page = 20
    search_fields = ['name','model','serial','asset_group__name','asset_brand__name']

@admin.register(AssetGroup)
class AssetGroupAdmin(BaseAdmin):
    list_display = ['name','remark']
    search_fields = ['name',]

@admin.register(AssetBrand)
class AssetBrandAdmin(BaseAdmin):
    list_display = ['name','remark']
    search_fields = ['name',]
