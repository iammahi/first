# Generated by Django 3.2 on 2021-06-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_rename_price1_types_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='conform_orders',
            name='advance',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conform_orders',
            name='payment_mode',
            field=models.CharField(default='Paid', max_length=50, null=True),
        ),
    ]
