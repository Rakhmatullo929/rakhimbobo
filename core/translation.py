from modeltranslation.translator import TranslationOptions, register
from .models import *


@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ('name', 'description')



@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'content')


@register(Article)
class ArticleTranslation(TranslationOptions):
    fields = ('title', 'content')


@register(Partner)
class PartnerTranslation(TranslationOptions):
    fields = ('name', 'description')


@register(TeamMember)
class TeamMemberTranslation(TranslationOptions):
    fields = ('name', 'bio')
