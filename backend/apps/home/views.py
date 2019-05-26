from django.shortcuts import render
from .models import Slide, Page


def index(request):
    """Показывает главную страницу."""
    page_data, created = Page.objects.get_or_create()
    return render(
        request,
        'home/index.html', {
            'slider': Slide.objects.filter(is_enabled=True).order_by('-weight'),
            'page_data': page_data
        }
    )
