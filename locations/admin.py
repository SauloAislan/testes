# Register your models here.
from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'device_id', 'lat', 'lng', 'status')