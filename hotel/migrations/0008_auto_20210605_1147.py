# Generated by Django 3.2 on 2021-06-05 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_conform_orders_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='types',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='types',
            name='price3',
        ),
    ]