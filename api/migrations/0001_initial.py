# Generated by Django 4.2.19 on 2025-02-13 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="HealthData",
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
                ("gender", models.CharField(max_length=10)),
                ("age", models.IntegerField()),
                ("weight", models.FloatField()),
                ("height", models.FloatField()),
                ("sleep_hours", models.FloatField()),
                ("water_intake", models.FloatField()),
                ("activity_level", models.CharField(max_length=50)),
                ("daily_steps", models.IntegerField()),
                ("stress_level", models.CharField(max_length=20)),
                ("health_conditions", models.TextField()),
                ("medications", models.TextField()),
                ("bad_habits", models.TextField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
