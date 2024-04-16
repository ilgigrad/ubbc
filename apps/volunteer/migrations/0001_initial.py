# Generated by Django 3.2.18 on 2024-04-03 09:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Volunteer",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="volunteer",
                        serialize=False,
                        to="user.user",
                        verbose_name="user",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("logistic", "logistic"),
                            ("control", "control"),
                            ("aid", "aid"),
                            ("supply", "supply"),
                            ("ground", "ground"),
                            ("undef", "undefine"),
                        ],
                        max_length=50,
                        verbose_name="role",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date create"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date update"
                    ),
                ),
            ],
            options={
                "verbose_name": "volunteer",
                "verbose_name_plural": "volunteers",
                "ordering": ["-created_at"],
                "get_latest_by": "created_at",
            },
        ),
    ]