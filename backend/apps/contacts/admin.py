from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import ContactsModel


@admin.register(ContactsModel)
class ContactsModelAdmin(SingleModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('map_code', 'contacts_code')
        }),
        ('SEO опции', {
            'classes': ('collapse',),
            'fields': ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description'),
        }),
    )
