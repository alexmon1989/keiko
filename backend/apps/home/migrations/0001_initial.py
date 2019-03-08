# Generated by Django 2.1.5 on 2019-02-11 13:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('title', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Заголовок')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(help_text='Размер: 1920px * 1080px', upload_to='', verbose_name='Изображение')),
                ('weight', models.IntegerField(default=1000, help_text='Чем выше вес, тем выше элемент в списке категорий.', verbose_name='Вес')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Включено')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайдер',
            },
        ),
    ]