# Generated by Django 5.1 on 2024-09-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_rename_customers_customer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="amount",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="transaction",
            name="trans_amount",
            field=models.IntegerField(null=True),
        ),
    ]
