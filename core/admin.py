from django.contrib import admin
from .models import Article, News, Partner, TeamMember, Contact, ContactMessage, Product
from modeltranslation.admin import TranslationAdmin


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(Partner)
class PartnerAdmin(TranslationAdmin):
    list_display = ('name', 'website', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'description')

@admin.register(TeamMember)
class TeamMemberAdmin(TranslationAdmin):
    list_display = ('name', 'position', 'order')
    list_filter = ('position',)
    list_editable = ('order',)
    search_fields = ('name', 'bio')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'is_new', 'is_available', 'created_at')
    list_filter = ('is_new', 'is_available', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created_at'
