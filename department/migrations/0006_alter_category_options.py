# Generated by Django 5.0.2 on 2024-02-21 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("department", "0005_property_want"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
    ]
