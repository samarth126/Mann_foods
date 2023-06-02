# Generated by Django 4.2 on 2023-05-21 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_ticket"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ticket",
            old_name="ticket_complain",
            new_name="description",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="ticket_user",
            new_name="user_distributor",
        ),
        migrations.AddField(
            model_name="ticket",
            name="closed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ticket",
            name="closed_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ticket",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2023, 5, 21, 8, 54, 24, 188532),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticket",
            name="subject",
            field=models.CharField(
                default=datetime.datetime(2023, 5, 21, 8, 54, 52, 272905),
                max_length=200,
            ),
            preserve_default=False,
        ),
    ]
