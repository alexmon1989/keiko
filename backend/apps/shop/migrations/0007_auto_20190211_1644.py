# Generated by Django 2.1.5 on 2019-02-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='shop.Category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='shop.Ingredient', verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='product',
            name='properties',
            field=models.ManyToManyField(blank=True, to='shop.Property', verbose_name='Свойства'),
        ),
    ]
