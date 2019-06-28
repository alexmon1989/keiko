from django import template
from django.contrib.sites.models import Site
from apps.settings.models import FooterContacts, SocialUrl, HeaderPhone

register = template.Library()


@register.inclusion_tag('footer_contacts.html')
def footer_contacts():
    data, created = FooterContacts.objects.get_or_create()
    return {
        'data': data
    }


@register.inclusion_tag('social_urls.html')
def social_urls():
    return {
        'urls': SocialUrl.objects.filter(is_enabled=True).order_by('-weight')
    }


@register.simple_tag()
def header_phone():
    phone, created = HeaderPhone.objects.get_or_create()
    return phone.value


@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')


@register.simple_tag
def current_domain():
    return "https://{}".format(Site.objects.get_current().domain)
