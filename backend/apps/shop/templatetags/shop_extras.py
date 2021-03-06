from django import template
from ..models import Category, Ingredient

register = template.Library()


@register.simple_tag
def categories():
    """Возвращает категории."""
    return Category.objects.filter(is_enabled=True).order_by('-weight')


@register.simple_tag
def ingredients():
    """Возвращает ингредиенты."""
    return Ingredient.objects.filter(is_enabled=True).order_by('-weight')


@register.inclusion_tag('shop/templatetags/markers.html')
def markers(product):
    return {
        'markers': product.markers.order_by('-weight')
    }
