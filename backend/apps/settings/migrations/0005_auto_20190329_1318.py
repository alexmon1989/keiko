# Generated by Django 2.1.5 on 2019-03-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_cardpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpayment',
            name='card_number',
            field=models.CharField(default='', max_length=255, verbose_name='Номер карты'),
        ),
    ]