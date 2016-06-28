from django.contrib import admin

from commons.admin import BaseAdmin
from .models import *

@admin.register(Warehouse)
class WarehouseAdmin(BaseAdmin):
    list_display = ['name','address','curator','remark']
    list_filter = ['curator__username']
    search_fields = ['name', 'curator__username', 'curator_first_name','contact__street','contact__post_code','contact__city']

@admin.register(WarehouseAssets)
class WarehouseAssetsAdmin(BaseAdmin):
    list_display = ['warehouse','asset','amount',"remark"]
    list_filter = ['asset__asset_brand__name', 'asset__asset_group__name', 'warehouse__name']
    search_fields = ['asset__asset_brand__brand__name', 'asset__asset_group__name', 'warehouse__name']

