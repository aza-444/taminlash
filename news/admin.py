from django.contrib import admin
from .models import NewsCategory, News, Video


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'published_date', 'is_featured', 'views']
    list_filter = ['category', 'is_featured', 'published_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']
    list_filter = ['published_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'published_date'
