# Generated by Django 2.1.5 on 2019-05-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_socialurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialurl',
            name='icon',
        ),
        migrations.AddField(
            model_name='socialurl',
            name='icon_class',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='CSS-класс иконки'),
        ),
    ]
