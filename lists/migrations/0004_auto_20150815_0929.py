# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lists.models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20150815_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.TextField(default=None, verbose_name=lists.models.List),
        ),
    ]
