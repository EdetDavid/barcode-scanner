# Generated by Django 4.2.5 on 2023-10-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Events",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("qr_code", models.ImageField(blank=True, upload_to="qr_code/")),
                ("date", models.DateField()),
            ],
        ),
    ]
