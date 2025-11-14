from modeltranslation.translator import register, TranslationOptions
from .models import Survey, SurveyChoice


@register(Survey)
class SurveyTranslationOptions(TranslationOptions):
    fields = ('question',)


@register(SurveyChoice)
class SurveyChoiceTranslationOptions(TranslationOptions):
    fields = ('choice_text',)
