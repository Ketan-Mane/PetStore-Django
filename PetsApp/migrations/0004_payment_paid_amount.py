# Generated by Django 4.2.5 on 2023-11-06 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetsApp', '0003_remove_payment_order_product_payment_order_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid_amount',
            field=models.FloatField(default=0),
        ),
    ]