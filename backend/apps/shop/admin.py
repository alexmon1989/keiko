from django.contrib import admin
from .models import Category, Product, Ingredient, Property, Order, CartProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Category."""
    ordering = ('-weight',)
    list_display = ('title', 'weight', 'is_enabled')
    list_editable = ('weight', 'is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Product."""
    ordering = ('title',)
    list_display = ('title', 'price', 'frontpad_id', 'is_enabled')
    list_editable = ('is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Ingredient."""
    list_display = ('title', 'weight', 'is_enabled')
    ordering = ('-weight',)
    list_editable = ('weight', 'is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Property."""
    ordering = ('title',)
    search_fields = ('title',)


class CartInline(admin.TabularInline):
    model = CartProduct
    extra = 1
    fields = ['product', 'price', 'count']
    verbose_name = "Продукт"
    verbose_name_plural = "Корзина"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Order."""
    inlines = [
        CartInline,
    ]
    exclude = ('cart',)
