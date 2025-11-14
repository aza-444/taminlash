from modeltranslation.translator import register, TranslationOptions
from .models import PowerPlant, KeyIndicator


@register(PowerPlant)
class PowerPlantTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'description')


@register(KeyIndicator)
class KeyIndicatorTranslationOptions(TranslationOptions):
    fields = ('title', 'unit')
