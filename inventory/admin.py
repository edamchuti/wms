from django.contrib import admin

from commons.admin import BaseAdmin  #,BulkBaseAdmin
from .models import *


@admin.register(Incoming)
class IncomingAdmin(BaseAdmin):
    list_display = ['asset','returned_by','received_by','amount','remark','return_date']
    search_fields = ['asset__name', 'returned_by__first_name','returned_by__last_name', 'received_by__username']
    exclude = ['createdby', 'modifiedby', 'deleted','received_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.createdby = request.user
        obj.modifiedby = request.user
        obj.received_by = request.user
        obj.save()


@admin.register(Outgoing)
class OutgoingAdmin(BaseAdmin):
    list_display = ['asset','assigned_to','assigned_by','amount','remark','assigned_date']
    search_fields = ['asset__name', 'assigned_to__first_name', 'assigned_to__last_name', 'assigned_by__username']
    exclude = ['createdby', 'modifiedby', 'deleted','assigned_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.createdby = request.user
        obj.modifiedby = request.user
        obj.assigned_by = request.user
        obj.save()


# class IncomingInline(admin.StackedInline):
#     model = Incoming
#     extra = 5
#
# class OutgoingInline(admin.StackedInline):
#     model = Outgoing
#     extra = 5

