# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0002_auto_20150718_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='illustration',
            field=models.ImageField(null=True, upload_to=b'static/media/illustration/%Y/%m', blank=True),
        ),
        migrations.AlterField(
            model_name='organisme',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'static/media/logo/%Y/%m', blank=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'static/media/photos/%Y/%m', blank=True),
        ),
    ]
