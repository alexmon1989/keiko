# Generated by Django 2.1.5 on 2019-03-12 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footercontacts',
            old_name='description',
            new_name='html',
        ),
    ]
