# Generated by Django 4.2.7 on 2023-11-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0019_alter_classattendancebybsm_class_attendance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]