from django.contrib import admin

from area.models import DhakaSubArea


# Register your models here.
class DhakaSubAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'bn_name', 'lat', 'lng')

    
admin.site.register(DhakaSubArea, DhakaSubAreaAdmin)
