# Generated by Django 2.1.5 on 2019-02-17 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_product_primary_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='primary_category',
            field=models.ForeignKey(blank=True, help_text='Для блока "Хлебные крошки"', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_category', to='shop.Category', verbose_name='Первичная категория'),
        ),
    ]
