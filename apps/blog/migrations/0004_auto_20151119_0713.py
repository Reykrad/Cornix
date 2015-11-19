# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151119_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]
