# Generated by Django 3.2 on 2021-06-12 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0013_alter_conform_orders_advance'),
    ]

    operations = [
        migrations.AddField(
            model_name='conform_orders',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]