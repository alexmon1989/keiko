# Generated by Django 2.1.5 on 2019-06-28 14:02

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('meta_h1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тег h1 (мета-тег)')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title (мета-тег)')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Keywords (мета-тег)')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description (мета-тег)')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, help_text='Размер: 450px * 450px', null=True, upload_to='', verbose_name='Изображение')),
                ('short_text', ckeditor.fields.RichTextField(blank=True, help_text='Отображается на странице со списком акций', null=True, verbose_name='Короткий текст')),
                ('full_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='Отображается на странице акции', null=True, verbose_name='Полный текст')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Включено')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]