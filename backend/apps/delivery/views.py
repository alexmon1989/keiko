from django.shortcuts import render
from .models import Page


def index(request):
    """Показывает страницу 'О доставке'."""
    page_data, created = Page.objects.get_or_create()
    return render(
        request,
        'delivery/index.html', {
            'page_data': page_data
        }
    )
