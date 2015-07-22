# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name=b'Date de d\xc3\xa9marrage')),
                ('duree', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('localisation', models.CharField(max_length=50)),
                ('illustration', models.ImageField(null=True, upload_to=b'media/illustration/%Y/%m')),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de cr\xc3\xa9ation fiche')),
                ('maj', models.DateTimeField(auto_now_add=True, verbose_name=b'Date de mise \xc3\xa0 jour fiche')),
                ('geom', django.contrib.gis.db.models.fields.PointField(default=b'SRID=3857;POINT(0.0 0.0)', srid=3857)),
            ],
            options={
                'ordering': ['-creation'],
                'verbose_name': 'action',
                'verbose_name_plural': 'actions',
            },
        ),
        migrations.CreateModel(
            name='avancement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40, choices=[('en attente', 'En attente'), ('initi\xe9', 'Initi\xe9'), ('\xe0 mi parcours', 'A mi parcours'), ('Termin\xe9', 'Termin\xe9')])),
            ],
            options={
                'verbose_name_plural': 'Avancements',
            },
        ),
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40, choices=[('environnement', 'Environnement'), ('tourisme', 'Tourisme'), ('d\xe9veloppement rural', 'D\xe9veloppement rural'), ('eau/assainissement', 'Eau/Assainissement'), ('sant\xe9', 'Sant\xe9'), ('\xe9ducation', '\xc9ducation'), ('justice', 'Justice'), ('formation conseil', 'Formation Conseil'), ('protection sociale', 'Protection Sociale'), ('micro-cr\xe9dit', 'Micro-Cr\xe9dit')])),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='organisme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40)),
                ('description', models.TextField(null=True)),
                ('logo', models.ImageField(null=True, upload_to=b'media/logo/%Y/%m')),
                ('referent', models.ForeignKey(blank=True, to='ong.organisme', null=True)),
            ],
            options={
                'ordering': ['nom'],
                'verbose_name': 'organisme',
                'verbose_name_plural': 'organismes',
            },
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=40, choices=[('ong', 'ONG'), ('bailleur', 'Bailleur'), ('organisation', 'Organisation')])),
            ],
            options={
                'verbose_name_plural': 'status',
            },
        ),
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(null=True, upload_to=b'media/photos/%Y/%m', blank=True)),
                ('is_responsable', models.BooleanField(default=False, verbose_name=b'Responsable autoris\xc3\xa9 \xc3\xa0 \xc3\xa9diter la fiche')),
                ('organisme', models.ForeignKey(to='ong.organisme')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'utilisateur',
                'verbose_name_plural': 'utilisateurs',
            },
        ),
        migrations.AddField(
            model_name='organisme',
            name='status',
            field=models.ForeignKey(verbose_name=b'status', to='ong.status'),
        ),
        migrations.AddField(
            model_name='action',
            name='avancement',
            field=models.ForeignKey(verbose_name=b"\xc3\xa9tat d'avancement", to='ong.avancement'),
        ),
        migrations.AddField(
            model_name='action',
            name='categories',
            field=models.ManyToManyField(to='ong.categorie', verbose_name=b'cat\xc3\xa9gorie'),
        ),
        migrations.AddField(
            model_name='action',
            name='organisme',
            field=models.ForeignKey(verbose_name=b"organisme maitre d'oeuvre", to='ong.organisme'),
        ),
        migrations.AddField(
            model_name='action',
            name='responsable',
            field=models.ForeignKey(verbose_name=b'nom du responsable de la fiche', to='ong.utilisateur'),
        ),
    ]
