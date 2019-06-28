from django.contrib import admin
from .models import PromotionArticle


@admin.register(PromotionArticle)
class PromotionArticleAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели PromotionArticle."""
    ordering = ('-created_at',)
    list_display = ('title', 'is_enabled', 'created_at', 'updated_at')
    list_editable = ('is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'image', 'short_text', 'full_text', 'is_enabled')
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )
