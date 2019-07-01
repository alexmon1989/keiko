from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import FooterContacts, RobotsTxt, SocialUrl, HeaderContact, Analytics
from apps.shop.models import DeliverySettings, CardPayment


@admin.register(Analytics)
class Analytics(SingleModelAdmin):
    pass


@admin.register(FooterContacts)
class FooterContactsAdmin(SingleModelAdmin):
    pass


@admin.register(DeliverySettings)
class DeliverySettingsAdmin(SingleModelAdmin):
    pass


@admin.register(CardPayment)
class CardPaymentAdmin(SingleModelAdmin):
    pass


@admin.register(RobotsTxt)
class RobotsTxtAdmin(SingleModelAdmin):
    pass


@admin.register(HeaderContact)
class HeaderContactAdmin(admin.ModelAdmin):
    ordering = ('pk',)
    list_display = ('value', 'is_phone_number')


@admin.register(SocialUrl)
class SocialUrlAdmin(admin.ModelAdmin):
    """Класс для описания интерфейса администрирования модели SocialUrl."""
    ordering = ('-weight',)
    list_display = ('social_network_title', 'url', 'weight', 'is_enabled')
    list_editable = ('weight', 'is_enabled',)
    list_filter = ('is_enabled',)
    search_fields = ('social_network_title',)
