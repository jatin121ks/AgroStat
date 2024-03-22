# Generated by Django 5.0.2 on 2024-02-10 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="person",
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
                ("F_name", models.CharField(max_length=35)),
                ("L_name", models.CharField(max_length=35)),
            ],
        ),
    ]
