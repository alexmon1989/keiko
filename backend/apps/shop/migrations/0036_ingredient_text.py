# Generated by Django 2.1.5 on 2019-06-21 12:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0035_category_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', null=True, verbose_name='Текст'),
        ),
    ]
