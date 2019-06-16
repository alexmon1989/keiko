from django import template
from ..models import Analytics

register = template.Library()


@register.simple_tag
def analytics():
    """Возвращает код аналитики."""
    a, created = Analytics.objects.get_or_create()
    return a.code
