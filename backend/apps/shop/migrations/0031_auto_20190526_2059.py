# Generated by Django 2.1.5 on 2019-05-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_marker_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='Description (мета-тег)'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_h1',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег h1 (мета-тег)'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Keywords (мета-тег)'),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title (мета-тег)'),
        ),
    ]