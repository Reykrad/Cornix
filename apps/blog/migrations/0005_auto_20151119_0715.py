# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151119_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='fecha_pub',
            field=models.DateField(auto_now=True),
        ),
    ]
