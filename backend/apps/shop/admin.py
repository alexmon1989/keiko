from django.contrib import admin
from .models import Category, Product, Ingredient, Property


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Category."""
    ordering = ('title',)
    list_display = ('title', 'is_enabled')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Product."""
    ordering = ('title',)
    list_display = ('title', 'price', 'frontpad_id', 'is_enabled')
    list_editable = ('is_enabled',)
    search_fields = ('title',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Ingredient."""
    ordering = ('title',)
    search_fields = ('title',)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Property."""
    ordering = ('title',)
    search_fields = ('title',)
