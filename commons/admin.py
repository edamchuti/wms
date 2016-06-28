from django.contrib import admin
from .models import *
# import bulk_admin

class BaseAdmin(admin.ModelAdmin):
    exclude = ['createdby', 'modifiedby', 'deleted']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.createdby = request.user
        obj.modifiedby = request.user
        obj.save()

@admin.register(Contact)
class ContactAdmin(BaseAdmin):
    list_display = ['email', 'address','mobile','phone', "remark"]
    search_fields = ['email', 'mobile', 'phone','post_code','street','city']


# class BulkAdmin(bulk_admin.BulkModelAdmin):
#     exclude = ['createdby', 'modifiedby', 'deleted']
#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.createdby = request.user
#         obj.modifiedby = request.user
#         obj.save()
