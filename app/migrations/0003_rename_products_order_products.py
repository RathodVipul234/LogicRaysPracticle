# Generated by Django 4.0.6 on 2022-07-23 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_brand_category_product_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Products',
            new_name='products',
        ),
    ]