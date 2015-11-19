# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151119_0819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
