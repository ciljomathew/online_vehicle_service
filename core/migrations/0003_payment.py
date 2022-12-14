# Generated by Django 4.1.2 on 2022-11-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_servicemodel_cost"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "pending"),
                            ("Completed", "completed"),
                            ("Failed", "failed"),
                        ],
                        default="pending",
                        max_length=16,
                    ),
                ),
                ("mode", models.CharField(blank=True, max_length=50, null=True)),
                ("razorpay_order_id", models.CharField(max_length=256)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
