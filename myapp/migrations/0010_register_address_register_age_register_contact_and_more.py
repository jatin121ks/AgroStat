# Generated by Django 5.0.2 on 2024-02-20 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0009_register"),
    ]

    operations = [
        migrations.AddField(
            model_name="register",
            name="address",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="register",
            name="age",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="register",
            name="contact",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="register",
            name="gender",
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]