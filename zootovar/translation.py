from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Cat)
class CatTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('filler', 'carrier',)



