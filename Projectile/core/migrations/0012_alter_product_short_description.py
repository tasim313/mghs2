# Generated by Django 4.2.2 on 2023-07-19 06:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_product_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="short_description",
            field=models.TextField(
                blank=True,
                max_length=500,
                null=True,
                validators=[django.core.validators.MinLengthValidator(11)],
            ),
        ),
    ]
