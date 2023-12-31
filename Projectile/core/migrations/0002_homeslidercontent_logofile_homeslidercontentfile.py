# Generated by Django 4.2.2 on 2023-07-11 04:59

import autoslug.fields
import core.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeSliderContent",
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
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        null=True,
                        populate_from=core.utils.get_home_slider_content_slug,
                        unique=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=30, verbose_name="Title"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(11)],
                    ),
                ),
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="LogoFile",
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
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True,
                        null=True,
                        upload_to=core.utils.get_website_logo_image,
                    ),
                ),
            ],
            bases=("core.basemodel",),
        ),
        migrations.CreateModel(
            name="HomeSliderContentFile",
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
                    "image",
                    versatileimagefield.fields.VersatileImageField(
                        blank=True,
                        null=True,
                        upload_to=core.utils.get_home_slider_content_image,
                    ),
                ),
                (
                    "home_content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="home_content_info",
                        to="core.homeslidercontent",
                    ),
                ),
            ],
            bases=("core.basemodel",),
        ),
    ]
