# Generated by Django 2.1.5 on 2019-05-29 19:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190526_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactsmodel',
            options={'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterField(
            model_name='contactsmodel',
            name='contacts_code',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Контактные данные'),
        ),
    ]