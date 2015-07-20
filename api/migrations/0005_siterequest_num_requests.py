# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_siterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='siterequest',
            name='num_requests',
            field=models.IntegerField(default=0),
        ),
    ]
