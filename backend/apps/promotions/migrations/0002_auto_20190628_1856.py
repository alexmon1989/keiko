# Generated by Django 2.1.5 on 2019-06-28 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='promotionarticle',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterField(
            model_name='promotionarticle',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]