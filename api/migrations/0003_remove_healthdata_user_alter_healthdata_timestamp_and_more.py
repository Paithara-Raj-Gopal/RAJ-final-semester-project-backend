# Generated by Django 4.2.19 on 2025-02-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_healthdata_timestamp_healthdata_username_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="healthdata", name="user",),
        migrations.AlterField(
            model_name="healthdata",
            name="timestamp",
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name="healthdata",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
