# Generated by Django 4.2.19 on 2025-02-13 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_healthdata_timestamp"),
    ]

    operations = [
        migrations.RemoveField(model_name="healthdata", name="id",),
        migrations.AlterField(
            model_name="healthdata",
            name="timestamp",
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name="healthdata",
            name="username",
            field=models.CharField(
                max_length=150, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
