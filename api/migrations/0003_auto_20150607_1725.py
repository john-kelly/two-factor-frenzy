# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_organization_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncryptionSupport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sha_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='encryption_support',
            field=models.OneToOneField(null=True, blank=True, to='api.EncryptionSupport'),
        ),
    ]
