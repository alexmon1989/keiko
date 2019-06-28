from django import template
from ..models import PromotionArticle

register = template.Library()


@register.inclusion_tag('promotions/templatetags/last_promotions.html')
def last_promotions():
    return {
        'promotions': PromotionArticle.objects.filter(is_enabled=True).order_by('-created_at')[:3]
    }
