# Generated by Django 4.2.4 on 2023-09-19 01:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assistance", "0016_alter_equipment_last_maintenance_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipment",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("new", "Novo"), ("semi-new", "Semi-novo")],
                max_length=20,
                null=True,
            ),
        ),
    ]