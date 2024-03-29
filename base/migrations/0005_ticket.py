# Generated by Django 4.2 on 2023-05-16 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_remove_distributor_applicants_applicant_storage_check_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ticket",
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
                ("ticket_complain", models.TextField()),
                (
                    "ticket_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.user_distributor",
                    ),
                ),
            ],
        ),
    ]
