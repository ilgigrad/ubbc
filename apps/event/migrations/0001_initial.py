# Generated by Django 3.2.18 on 2024-04-03 09:31

import uuid

import core.utils.colors
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields
import event.models._event_edition
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Edition",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("date", models.DateField(blank=True, null=True, verbose_name="date")),
                (
                    "year",
                    models.IntegerField(
                        default=event.models._event_edition.get_year,
                        verbose_name="year",
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
                "verbose_name": "edition",
                "verbose_name_plural": "editions",
                "ordering": ["-created_at"],
                "get_latest_by": "created_at",
            },
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("logo", models.ImageField(blank=True, null=True, upload_to="logo/")),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                (
                    "description",
                    models.TextField(
                        blank=True, max_length=1000, verbose_name="description"
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("fr-FR", "french"),
                            ("en-GB", "english (UK)"),
                            ("en-US", "english (USA)"),
                            ("es-ES", "spanish"),
                            ("pt-BR", "brazilian portuguese"),
                            ("zh-CN", "chinese"),
                            ("nl-NL", "dutch"),
                            ("fr-CA", "canadian french"),
                            ("fi-FI", "finnish"),
                            ("de-DE", "german"),
                            ("it-IT", "italian"),
                            ("ja-JP", "japanese"),
                            ("ko-KR", "korean"),
                            ("pl-PL", "polish"),
                            ("pt-PT", "portuguese"),
                            ("ru-RU", "russian"),
                            ("bg-BG", "bulgarian"),
                            ("hr-HR", "croatian"),
                            ("cs-CZ", "czech"),
                            ("da-DK", "danish"),
                            ("et-EE", "estonian"),
                            ("el-GR", "greek"),
                            ("hu-HU", "hungarian"),
                            ("lv-LV", "latvian"),
                            ("lt-LT", "lithuanian"),
                            ("mt-MT", "maltese"),
                            ("ro-RO", "romanian"),
                            ("sk-SK", "slovak"),
                            ("sl-SI", "slovene"),
                            ("sv-SE", "swedish"),
                            ("iw-IL", "hebrew"),
                            ("nb-NO", "norwegian (bokmål)"),
                            ("ar-SA", "arabic saudi arabia"),
                            ("ar-QA", "arabic qatar"),
                            ("ar-AE", "arabic united arab emirates"),
                            ("ar-DZ", "arabic algeria"),
                            ("ar-MA", "arabic morocco"),
                            ("ar-EG", "arabic egypt"),
                            ("ar-IL", "arabic israel"),
                            ("ar-JO", "arabic jordan"),
                            ("ar-KW", "arabic kuwait"),
                            ("ar-LB", "arabic lebanon"),
                            ("lo-LO", "lorem ipsum"),
                        ],
                        default="en",
                        max_length=10,
                        verbose_name="prefered language",
                    ),
                ),
                (
                    "website",
                    models.URLField(blank=True, null=True, verbose_name="website"),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="email"
                    ),
                ),
                (
                    "telephone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="telephone",
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="zip code"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=50, verbose_name="city"),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        max_length=2, verbose_name="country"
                    ),
                ),
                (
                    "sports",
                    multiselectfield.db.fields.MultiSelectField(
                        blank=True,
                        choices=[
                            ("running", "running"),
                            ("trail", "trail running"),
                            ("ultra", "ultra trail"),
                            ("atle", "athletism"),
                            ("foot", "football"),
                            ("tennis", "tennis"),
                            ("bike", "bicycling"),
                            ("swim", "swimming"),
                            ("triathlon", "triathlon"),
                            ("skimo", "ski mountaining"),
                            ("ski", "ski"),
                            ("hike", "hiking"),
                            ("vertical", "vertical running"),
                            ("mb", "mountain biking"),
                            ("gravel", "gravel biking"),
                            ("canoe", "canoe"),
                            ("kayak", "kayak"),
                            ("nordic", "nordic ski"),
                            ("skate", "inline skate"),
                            ("rugby", "rugby"),
                            ("rugby14", "rugby 14"),
                            ("rugby7", "rugby 7"),
                            ("foot7", "fottball 7"),
                            ("foot5", "football 5"),
                        ],
                        default=[],
                        max_length=148,
                        null=True,
                        verbose_name="sports",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        blank=True,
                        default=core.utils.colors.random_color,
                        max_length=7,
                        verbose_name="color",
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
                "verbose_name": "event",
                "verbose_name_plural": "events",
                "ordering": ["-created_at"],
                "get_latest_by": "created_at",
            },
        ),
        migrations.CreateModel(
            name="Organizer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("admin", "administrator"),
                            ("super", "supervisor"),
                            ("edit", "editor"),
                            ("undef", "undefine"),
                        ],
                        max_length=20,
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
                (
                    "event",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organizers",
                        to="event.event",
                        verbose_name="event",
                    ),
                ),
            ],
            options={
                "verbose_name": "organizer",
                "verbose_name_plural": "organizers",
                "ordering": ["-created_at"],
                "get_latest_by": "created_at",
            },
        ),
    ]