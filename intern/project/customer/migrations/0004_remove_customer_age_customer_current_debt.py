# Generated by Django 4.2.9 on 2024-01-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_customer_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='age',
        ),
        migrations.AddField(
            model_name='customer',
            name='current_debt',
            field=models.FloatField(null=True),
        ),
    ]
