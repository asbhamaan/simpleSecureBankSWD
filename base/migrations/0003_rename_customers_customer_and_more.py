# Generated by Django 5.1 on 2024-09-02 13:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_account_transactions_alter_customers_custid"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="customers",
            new_name="customer",
        ),
        migrations.RenameModel(
            old_name="transactions",
            new_name="transaction",
        ),
    ]
