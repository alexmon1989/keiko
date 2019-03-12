from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import FooterContacts


@admin.register(FooterContacts)
class FooterContactsAdmin(SingleModelAdmin):
    pass
