# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20141218_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='state',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
