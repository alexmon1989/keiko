# Generated by Django 2.1.5 on 2019-02-17 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='primary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_category', to='shop.Category', verbose_name='Первичная категория'),
        ),
    ]
