from django.contrib import admin
from .models import Slide


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Category."""
    ordering = ('-weight',)
    list_display = ('title', 'link', 'weight', 'is_enabled')
    list_editable = ('weight', 'is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)
