# Generated by Django 4.2.16 on 2024-12-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=30)),
                ("no", models.CharField(max_length=30)),
                ("marks", models.FloatField(max_length=30)),
                ("addr", models.CharField(max_length=30)),
            ],
        ),
    ]
