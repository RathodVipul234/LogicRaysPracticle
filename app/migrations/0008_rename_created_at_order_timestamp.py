# Generated by Django 4.0.6 on 2022-07-23 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_order_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='timestamp',
        ),
    ]
