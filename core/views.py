from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Article, News, Partner, TeamMember, Contact, ContactMessage, Product
from .forms import ContactMessageForm

def home(request):
    latest_articles = Article.objects.filter(is_published=True)[:3]
    latest_news = News.objects.filter(is_published=True)[:3]
    featured_products = Product.objects.filter(is_available=True)[:3]
    
    try:
        contact_info = Contact.objects.first()
    except Contact.DoesNotExist:
        contact_info = None
    
    context = {
        'latest_articles': latest_articles,
        'latest_news': latest_news,
        'products': featured_products,
        'contact_info': contact_info,
        'title': 'Dry Fruta - Premium Dried Fruits',
    }
    return render(request, 'core/home.html', context)

def articles_news(request):
    articles = Article.objects.filter(is_published=True)
    news = News.objects.filter(is_published=True)
    
    context = {
        'articles': articles,
        'news': news,
        'title': 'Articles & News - Dry Fruta',
    }
    return render(request, 'core/articles_news.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    
    # Get other recent articles excluding current one
    related_articles = Article.objects.filter(is_published=True).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
        'title': f'{article.title} - Dry Fruta',
    }
    return render(request, 'core/article_detail.html', context)

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug, is_published=True)
    
    # Get other recent news excluding current one
    news_recent = News.objects.filter(is_published=True).exclude(id=news_item.id)[:3]
    
    context = {
        'news_item': news_item,
        'news_recent': news_recent,
        'title': f'{news_item.title} - Dry Fruta',
    }
    return render(request, 'core/news_detail.html', context)

def partners(request):
    partners_list = Partner.objects.all()
    
    context = {
        'partners': partners_list,
        'title': 'Our Partners - Dry Fruta',
    }
    return render(request, 'core/partners.html', context)

def leadership(request):
    team_members = TeamMember.objects.all()
    
    context = {
        'team_members': team_members,
        'title': 'Leadership - Dry Fruta',
    }
    return render(request, 'core/leadership.html', context)

def contacts(request):
    try:
        contact_info = Contact.objects.first()
    except Contact.DoesNotExist:
        contact_info = None
    
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('core:contacts')
    else:
        form = ContactMessageForm()
    
    context = {
        'contact_info': contact_info,
        'form': form,
        'title': 'Contact Us - Dry Fruta',
    }
    return render(request, 'core/contacts.html', context)

def products(request):
    products_list = Product.objects.filter(is_available=True)
    
    context = {
        'products': products_list,
        'title': 'Our Products - Dry Fruta',
    }
    return render(request, 'core/products.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Return JSON for modal
        product_data = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(product.price),
            'image': product.image.url if product.image else None,
            'is_new': product.is_new,
        }
        return JsonResponse(product_data)
    
    # Regular view (fallback)
    context = {
        'product': product,
        'title': f'{product.name} - Dry Fruta',
    }
    return render(request, 'core/product_detail.html', context)
