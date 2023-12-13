# Generated by Django 4.2.2 on 2023-07-26 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0031_productdetails"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productdetails",
            name="title",
            field=models.CharField(
                blank=True,
                db_index=True,
                max_length=100,
                null=True,
                verbose_name="Title",
            ),
        ),
    ]
