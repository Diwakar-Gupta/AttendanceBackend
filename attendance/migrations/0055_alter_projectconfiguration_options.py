# Generated by Django 4.2.8 on 2024-02-17 21:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0054_alter_projectconfiguration_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="projectconfiguration",
            options={
                "permissions": [
                    ("can_sync_to_gsheet", "Can Sync Attendance with Gsheet")
                ]
            },
        ),
    ]