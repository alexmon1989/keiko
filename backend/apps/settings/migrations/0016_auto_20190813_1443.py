# Generated by Django 2.1.5 on 2019-08-13 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0015_auto_20190813_1437'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CardPayment',
            new_name='Payment',
        ),
    ]