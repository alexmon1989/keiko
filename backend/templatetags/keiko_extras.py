from django import template
from django.contrib.sites.models import Site
from apps.settings.models import FooterContacts, SocialUrl, HeaderContact

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


@register.inclusion_tag('header_contacts.html')
def header_contacts():
    return {'contacts': HeaderContact.objects.order_by('pk')}


@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')


@register.simple_tag
def current_domain():
    return "https://{}".format(Site.objects.get_current().domain)


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
