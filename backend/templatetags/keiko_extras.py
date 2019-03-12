from django import template
from apps.settings.models import FooterContacts

register = template.Library()


@register.inclusion_tag('footer_contacts.html')
def footer_contacts():
    data, created = FooterContacts.objects.get_or_create()
    return {
        'data': data
    }
