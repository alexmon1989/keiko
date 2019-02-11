from django.shortcuts import render
from .models import Slide


def index(request):
    """Показывает главную страницу."""
    return render(request, 'home/index.html', {'slider': Slide.objects.filter(is_enabled=True).order_by('-weight')})
