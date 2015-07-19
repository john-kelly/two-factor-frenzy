# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150607_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Received'), (1, b'In Progress'), (2, b'Completed'), (-1, b'Rejected')])),
                ('notes', models.CharField(default=b'', max_length=256)),
            ],
        ),
    ]
