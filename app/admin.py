from django.contrib import admin
from django.http import HttpRequest
from app.models import GeneralInfo, Service

# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    # pass
    list_display = ['company_name', 'location', 'phone', 'email', 'open_hours']
    # search_fields = ('company_name', 'location')
    # list_filter = ('company_name', 'location')

    # #show to disable add permission 
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    #show to disable update permission
    # def has_change_permission(self, request, obj= None):
    #     return False

    #show to disable delete permission
    # def has_delete_permission(self, request, obj= None):
    #     return False
    
    # #show you can set field to disable update
    # readonly_fields = ['email']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'icon']