from django.contrib import admin
from .models import PowerPlant, KeyIndicator


@admin.register(PowerPlant)
class PowerPlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'plant_type', 'capacity', 'location', 'is_active']
    list_filter = ['plant_type', 'is_active']
    search_fields = ['name', 'location']


@admin.register(KeyIndicator)
class KeyIndicatorAdmin(admin.ModelAdmin):
    list_display = ['title', 'value', 'unit', 'year', 'order']
    list_filter = ['year']
    ordering = ['order']
