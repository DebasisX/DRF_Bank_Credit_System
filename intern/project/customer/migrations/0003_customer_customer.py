# Generated by Django 4.2.9 on 2024-01-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_approved_limit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer',
            field=models.IntegerField(default=1),
        ),
    ]
