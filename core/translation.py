from modeltranslation.translator import register, TranslationOptions
from .models import CarouselSlide, QuickLink, GovernmentLink, CompanyHistory


@register(CarouselSlide)
class CarouselSlideTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(QuickLink)
class QuickLinkTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(GovernmentLink)
class GovernmentLinkTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(CompanyHistory)
class CompanyHistoryTranslationOptions(TranslationOptions):
    fields = ('content',)
