from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles-news/', views.articles_news, name='articles_news'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('partners/', views.partners, name='partners'),
    path('leadership/', views.leadership, name='leadership'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
] 