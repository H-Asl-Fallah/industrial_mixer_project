from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    """
    این ویو لیست تمام مقالات منتشر شده را نمایش می‌دهد.
    """
    articles = Article.objects.filter(status='published')
    return render(request, '../templates/article_list.html', {'articles': articles})

def article_detail(request, slug):
    """
    این ویو جزئیات یک مقاله خاص را بر اساس اسلاگ آن نمایش می‌دهد.
    """
    article = get_object_or_404(Article, slug=slug, status='published')
    return render(request, '../templates/article_detail.html', {'article': article})