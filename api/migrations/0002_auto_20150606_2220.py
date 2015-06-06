# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfasupport',
            name='documentation',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='twitter_handle',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(null=True, blank=True),
        ),
    ]
