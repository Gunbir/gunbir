# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20141219_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='update',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
