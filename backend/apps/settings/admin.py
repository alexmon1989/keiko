from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import FooterContacts
from apps.shop.models import DeliverySettings, CardPayment


@admin.register(FooterContacts)
class FooterContactsAdmin(SingleModelAdmin):
    pass


@admin.register(DeliverySettings)
class DeliverySettingsAdmin(SingleModelAdmin):
    pass


@admin.register(CardPayment)
class CardPaymentAdmin(SingleModelAdmin):
    pass
