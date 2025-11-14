from modeltranslation.translator import register, TranslationOptions
from .models import NewsCategory, News, Video


@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'excerpt')


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
