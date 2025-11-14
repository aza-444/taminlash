from django.contrib import admin
from .models import CarouselSlide, QuickLink, GovernmentLink, CompanyHistory


@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']


@admin.register(QuickLink)
class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']


@admin.register(GovernmentLink)
class GovernmentLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'order', 'is_active']
    list_filter = ['is_active']
    ordering = ['order']


@admin.register(CompanyHistory)
class CompanyHistoryAdmin(admin.ModelAdmin):
    list_display = ['year_start', 'updated_at']
