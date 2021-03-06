# Generated by Django 2.1.5 on 2019-03-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0028_product_weight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(blank=True, help_text='Размер: 40px * 30px', null=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Маркер',
                'verbose_name_plural': 'Маркеры',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_hit',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_new',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_spicy',
        ),
        migrations.AddField(
            model_name='product',
            name='markers',
            field=models.ManyToManyField(blank=True, to='shop.Marker', verbose_name='Маркеры'),
        ),
    ]
