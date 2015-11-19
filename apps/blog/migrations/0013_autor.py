# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_auto_20151119_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter', models.URLField(max_length=130, null=True)),
                ('facebook', models.URLField(null=True)),
                ('youtube', models.URLField(null=True)),
                ('github', models.URLField(max_length=130, null=True)),
                ('sitioweb', models.URLField(max_length=130, null=True)),
                ('desb', models.TextField(max_length=500, null=True)),
                ('desl', models.TextField(null=True)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
