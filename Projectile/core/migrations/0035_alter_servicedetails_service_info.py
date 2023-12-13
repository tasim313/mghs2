# Generated by Django 4.2.2 on 2023-07-26 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0034_servicedetails"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servicedetails",
            name="service_info",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="service_details_info",
                to="core.service",
            ),
        ),
    ]
