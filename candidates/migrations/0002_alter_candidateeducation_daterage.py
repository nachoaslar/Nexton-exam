# Generated by Django 5.1.1 on 2025-02-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidateeducation",
            name="dateRage",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
