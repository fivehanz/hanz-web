# Generated by Django 5.0.1 on 2024-01-17 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_formpage_formfield"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
    ]

    operations = [
        migrations.CreateModel(
            name="GoogleTagManagerSettings",
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
                (
                    "google_tag_manager_id",
                    models.CharField(
                        blank=True,
                        help_text='Begins with "GTM-"',
                        max_length=255,
                        verbose_name="Google Tag Manager ID",
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Google Tag Manager",
            },
        ),
    ]