# Generated by Django 4.0.6 on 2022-07-23 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_order_total_price_alter_order_total_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_qty',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
