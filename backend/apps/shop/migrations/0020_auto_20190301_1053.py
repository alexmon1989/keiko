# Generated by Django 2.1.5 on 2019-03-01 08:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_order_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
