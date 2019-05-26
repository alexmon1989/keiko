from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import ContactsModel


@admin.register(ContactsModel)
class ContactsModelAdmin(SingleModelAdmin):
    pass
