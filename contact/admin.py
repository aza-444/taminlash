from django.contrib import admin
from .models import ContactMessage, Survey, SurveyChoice, SurveyResponse, HelplineStats


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['full_name', 'email', 'subject', 'message']
    readonly_fields = ['created_at']


class SurveyChoiceInline(admin.TabularInline):
    model = SurveyChoice
    extra = 2


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['question', 'step_number', 'is_active']
    list_filter = ['is_active']
    inlines = [SurveyChoiceInline]


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ['survey', 'choice', 'submitted_at', 'ip_address']
    list_filter = ['survey', 'submitted_at']
    readonly_fields = ['submitted_at']


@admin.register(HelplineStats)
class HelplineStatsAdmin(admin.ModelAdmin):
    list_display = ['total_calls', 'rating_5', 'rating_4', 'rating_3', 'rating_2', 'rating_1', 'updated_at']
