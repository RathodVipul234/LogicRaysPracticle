# Generated by Django 4.0.6 on 2022-07-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_userotp_invalid_attempt_userotp_is_expired_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userotp',
            name='invalid_attempt',
            field=models.IntegerField(default=0),
        ),
    ]