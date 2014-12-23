# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20141219_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='state',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
