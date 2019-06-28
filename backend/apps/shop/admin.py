from django.contrib import admin
from .models import Category, Product, Ingredient, Property, Order, OrderStatus, CartProduct, Marker


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Category."""
    ordering = ('-weight',)
    list_display = ('title', 'weight', 'is_enabled')
    list_editable = ('weight', 'is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'weight', 'image', 'text', 'is_enabled')
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Product."""
    ordering = ('title',)
    list_display = ('title', 'slug', 'weight', 'price', 'primary_category', 'frontpad_id', 'is_enabled')
    list_editable = ('is_enabled', 'weight',)
    list_filter = ('is_enabled', 'primary_category',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'slug',
                'weight',
                'image',
                'description_short',
                'description',
                'primary_category',
                'categories',
                'properties',
                'ingredients',
                'price',
                'related_products',
                'markers',
                'frontpad_id',
                'is_enabled',
            )
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Ingredient."""
    list_display = ('title', 'weight', 'is_enabled')
    ordering = ('-weight',)
    list_editable = ('weight', 'is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'weight', 'image', 'tags', 'text', 'is_enabled')
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )


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
    list_display = ('user_name', 'created_at', 'user_email', 'user_phone', 'pay_mode', 'paid', 'delivery_mode',
                    'get_price_total', 'status', 'frontpad_id')
    readonly_fields = ('get_price_total',)

    def get_price_total(self, obj):
        """Возвращает стоимость заказа."""
        return f"{obj.get_price_total()} руб."

    get_price_total.short_description = 'Стоимость заказа'
    get_price_total.admin_order_field = 'get_price_total'


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели OrderStatus."""
    search_fields = ('title',)
    list_display = ('title', 'color')
    ordering = ('pk',)


@admin.register(Marker)
class IconAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели Marker."""
    search_fields = ('title',)
    list_display = ('title', 'weight')
    list_editable = ('weight',)
    ordering = ('title',)
