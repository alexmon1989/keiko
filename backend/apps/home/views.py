from django.shortcuts import render


def index(request):
    """Показывает главную страницу."""
    return render(request, 'home/index.html')
