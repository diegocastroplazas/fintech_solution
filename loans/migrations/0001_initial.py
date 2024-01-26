# Generated by Django 5.0.1 on 2024-01-26 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Loan",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("external_id", models.CharField(max_length=60, unique=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[
                            (1, "Pending"),
                            (2, "Active"),
                            (3, "Rejected"),
                            (4, "Paid"),
                        ],
                        default=1,
                    ),
                ),
                ("contract_version", models.CharField(max_length=30)),
                ("maximum_payment_date", models.DateTimeField(blank=True, null=True)),
                ("taken_at", models.DateTimeField(blank=True, null=True)),
                (
                    "outstanding_amount",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="customers.customer",
                    ),
                ),
            ],
            options={
                "db_table": "loans",
                "ordering": ["id"],
            },
        ),
    ]
