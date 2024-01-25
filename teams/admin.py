
from django.contrib import admin

from . import models
from .models import Role, Location

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'location', 'start_date' ]
    list_editable = ['role', 'location']

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'role':
    #         kwargs['queryset'] = Role.objects.all()  # Replace 'Role' with the actual name of your Role model
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['type']
    #list_editable = ['type']
    list_display_links = ['type']


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['building']
    #list_editable = ['building']
    list_display_links = ['building']
    






    
#admin.site.register(Location)