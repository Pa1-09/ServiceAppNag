# Generated by Django 4.1.7 on 2023-02-26 05:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("Orders", "0003_alter_representative_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="representative",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="representative",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("50874969-6648-4c32-89da-7db377fcdf53"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]