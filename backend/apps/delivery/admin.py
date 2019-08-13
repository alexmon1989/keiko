from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from .models import Page


@admin.register(Page)
class Page(SingleModelAdmin):
    pass
