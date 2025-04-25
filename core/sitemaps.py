from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Article, News

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    
    def items(self):
        return ['core:home', 'core:articles_news', 'core:partners', 'core:leadership', 'core:contacts']
    
    def location(self, item):
        return reverse(item)

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = 'https'
    
    def items(self):
        return Article.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
        
    def location(self, obj):
        return reverse('core:article_detail', kwargs={'slug': obj.slug})

class NewsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7
    protocol = 'https'
    
    def items(self):
        return News.objects.all()
    
    def lastmod(self, obj):
        return obj.updated_at
        
    def location(self, obj):
        return reverse('core:news_detail', kwargs={'slug': obj.slug}) 