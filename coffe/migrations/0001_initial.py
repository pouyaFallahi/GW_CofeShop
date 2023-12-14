# Generated by Django 5.0 on 2023-12-09 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=12)),
                ("gender", models.CharField(max_length=12)),
                ("address", models.TextField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=50)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=12)),
                ("gender", models.CharField(max_length=12)),
                ("address", models.TextField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=50)),
                ("role", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Manager",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=12)),
                ("gender", models.CharField(max_length=12)),
                ("address", models.TextField()),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("username", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=50)),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="managers",
                        to="coffe.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
