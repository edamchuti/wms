from django.contrib import admin

from commons.admin import BaseAdmin
from .models import *

@admin.register(PersonType)
class PersonTypeAdmin(BaseAdmin):
    list_display = ['name','remark']
    search_fields = ['name', 'remark']

@admin.register(Person)
class PersonAdmin(BaseAdmin):
    list_display = ['name','person_type','contact']
    search_fields = ['name', 'person_type__name', 'contact__email', 'contact__mobile', 'contact__phone']

