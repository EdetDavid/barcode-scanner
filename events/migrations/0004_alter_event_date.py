# Generated by Django 4.2.5 on 2023-10-11 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0003_alter_event_qr_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]