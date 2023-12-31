# Generated by Django 4.2.2 on 2023-07-18 14:36

import core.utils
from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_testimonials"),
    ]

    operations = [
        migrations.AddField(
            model_name="testimonials",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True, null=True, upload_to=core.utils.get_testimonial_image
            ),
        ),
    ]
