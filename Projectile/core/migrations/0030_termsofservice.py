# Generated by Django 4.2.2 on 2023-07-25 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0029_privacypolicy"),
    ]

    operations = [
        migrations.CreateModel(
            name="TermsOfService",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=300)),
                (
                    "description",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
            ],
            bases=("core.basemodel",),
        ),
    ]
