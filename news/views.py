from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News, NewsCategory, Video


def news_list(request):
    news_list = News.objects.all()
    categories = NewsCategory.objects.all()
    videos = Video.objects.all()[:4]
    
    paginator = Paginator(news_list, 9)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'news': news,
        'categories': categories,
        'videos': videos,
    }
    return render(request, 'news/list.html', context)


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    news.views += 1
    news.save()
    
    related_news = News.objects.filter(category=news.category).exclude(id=news.id)[:3]
    
    context = {
        'news': news,
        'related_news': related_news,
    }
    return render(request, 'news/detail.html', context)


def news_by_category(request, slug):
    category = get_object_or_404(NewsCategory, slug=slug)
    news_list = News.objects.filter(category=category)
    categories = NewsCategory.objects.all()
    
    paginator = Paginator(news_list, 9)
    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    
    context = {
        'news': news,
        'category': category,
        'categories': categories,
    }
    return render(request, 'news/list.html', context)
