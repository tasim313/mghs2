# Generated by Django 4.2.2 on 2023-07-23 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_aboutfile"),
    ]

    operations = [
        migrations.CreateModel(
            name="WhyChooseUs",
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
                (
                    "headline",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Content Title"
                    ),
                ),
                (
                    "short_description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="WhyChooseUsSubContent",
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
                (
                    "headline",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="Content Title"
                    ),
                ),
                (
                    "short_description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "content",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.whychooseus",
                    ),
                ),
            ],
            bases=("core.basemodel",),
        ),
    ]