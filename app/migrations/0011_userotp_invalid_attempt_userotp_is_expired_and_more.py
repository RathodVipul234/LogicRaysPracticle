# Generated by Django 4.0.6 on 2022-07-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_order_total_price_alter_order_total_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='userotp',
            name='invalid_attempt',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userotp',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
