from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Slide, Page


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Category."""
    ordering = ('-weight',)
    list_display = ('title', 'link', 'weight', 'is_enabled')
    list_editable = ('weight', 'is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)


@admin.register(Page)
class Page(SingleModelAdmin):
    exclude = ('meta_h1', )
