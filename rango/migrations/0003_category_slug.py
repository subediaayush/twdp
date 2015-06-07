# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150605_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, default=datetime.datetime(2015, 6, 5, 13, 38, 6, 43022, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
