# Generated by Django 2.1.5 on 2019-02-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='Размер: 100px * 64px', null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='image',
            field=models.ImageField(blank=True, help_text='Размер: 100px * 64px', null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='is_enabled',
            field=models.BooleanField(default=True, verbose_name='Включено'),
        ),
    ]
