from django.shortcuts import render
from .models import CarouselSlide, QuickLink, GovernmentLink, CompanyHistory
from news.models import News
from powerplants.models import PowerPlant, KeyIndicator
from contact.models import HelplineStats


def homepage(request):
    context = {
        'carousel_slides': CarouselSlide.objects.filter(is_active=True)[:4],
        'quick_links': QuickLink.objects.filter(is_active=True)[:6],
        'news': News.objects.filter(is_featured=True)[:4],
        'latest_news': News.objects.all()[:3],
        'key_indicators': KeyIndicator.objects.all()[:4],
        'power_plants': PowerPlant.objects.filter(is_active=True),
        'government_links': GovernmentLink.objects.filter(is_active=True)[:10],
        'helpline_stats': HelplineStats.objects.first(),
    }
    return render(request, 'home.html', context)


def history_page(request):
    context = {
        'history': CompanyHistory.objects.first(),
    }
    return render(request, 'history.html', context)
