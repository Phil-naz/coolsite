from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Books)
class BooksTranslationOptions(TranslationOptions):
    fields = ('name', 'author', 'author_description')


@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
