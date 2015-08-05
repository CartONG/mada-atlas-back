# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='avancement',
            field=models.ForeignKey(to='ong.avancement', to_field=b'nom', verbose_name=b"\xc3\xa9tat d'avancement"),
        ),
        migrations.AlterField(
            model_name='action',
            name='organisme',
            field=models.ForeignKey(to='ong.organisme', to_field=b'nom', verbose_name=b"organisme maitre d'oeuvre"),
        ),
    ]
