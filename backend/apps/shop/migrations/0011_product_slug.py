# Generated by Django 2.1.5 on 2019-02-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20190212_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]
