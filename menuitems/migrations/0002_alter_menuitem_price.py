# Generated by Django 4.1.2 on 2022-10-12 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menuitems", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="price",
            field=models.FloatField(max_length=8),
        ),
    ]
