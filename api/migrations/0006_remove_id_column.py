from django.db import migrations

def remove_id_column(apps, schema_editor):
    # Custom SQL to drop the `id` column if it exists
    schema_editor.execute('ALTER TABLE api_healthdata DROP COLUMN IF EXISTS id;')

class Migration(migrations.Migration):

    dependencies = [
        # Replace with the previous migration file that should come before this one.
        ('api', '0005_remove_healthdata_id_alter_healthdata_timestamp_and_more'),
    ]

    operations = [
        migrations.RunPython(remove_id_column),
    ]
