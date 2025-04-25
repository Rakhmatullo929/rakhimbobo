from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticSitemap, ArticleSitemap, NewsSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticSitemap,
    'articles': ArticleSitemap,
    'news': NewsSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls', namespace='core')),
    path('set_language/', set_language, name='set_language'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Dry Fruta"
admin.site.site_title = "Dry Fruta"
admin.site.index_title = "Dry Fruta"