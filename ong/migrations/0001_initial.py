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
                ('date', models.DateField(verbose_name=b'Date de d\xc3\xa9marrage')),
                ('duree', models.CharField(max_length=40, null=True, blank=True)),
                ('description', models.TextField(null=True)),
                ('localisation', models.CharField(max_length=50)),
                ('illustration', models.ImageField(null=True, upload_to=b'static/media/illustration/%Y/%m', blank=True)),
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
                ('nom', models.CharField(unique=True, max_length=40, choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Termin\xe9', 'Termin\xe9')])),
            ],
            options={
                'verbose_name_plural': 'Avancements',
            },
        ),
        migrations.CreateModel(
            name='categorie',
            fields=[
                ('nom', models.CharField(max_length=40, serialize=False, primary_key=True, choices=[('Environnement', 'Environnement'), ('Tourisme', 'Tourisme'), ('D\xe9veloppement rural', 'D\xe9veloppement rural'), ('Eau, assainissement et hygi\xe8ne', 'Eau, assainissement et hygi\xe8ne'), ('Sant\xe9', 'Sant\xe9'), ('\xc9ducation', '\xc9ducation'), ("Droits de l'Homme", "Droits de l'Homme"), ('D\xe9veloppement \xe9conomique', 'D\xe9veloppement \xe9conomique'), ('Protection sociale', 'Protection Sociale'), ('Micro-cr\xe9dit', 'Micro-Cr\xe9dit')])),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='organisme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(unique=True, max_length=40)),
                ('description', models.TextField(null=True)),
                ('logo', models.ImageField(null=True, upload_to=b'static/media/logo/%Y/%m', blank=True)),
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
                ('nom', models.CharField(unique=True, max_length=40, choices=[('Partenaire sur une action', 'Partenaire'), ('Bailleur', 'Bailleur'), ("Organisme ma\xeetre d'oeuvre", 'Organisme')])),
            ],
            options={
                'verbose_name_plural': 'status',
            },
        ),
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(null=True, upload_to=b'static/media/photos/%Y/%m', blank=True)),
                ('is_responsable', models.BooleanField(default=False, verbose_name=b'Responsable autoris\xc3\xa9 \xc3\xa0 \xc3\xa9diter la fiche')),
                ('organisme', models.ForeignKey(to='ong.organisme')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field=b'username')),
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
            field=models.ForeignKey(to='ong.status', to_field=b'nom', verbose_name=b'status'),
        ),
        migrations.AddField(
            model_name='action',
            name='avancement',
            field=models.OneToOneField(verbose_name=b"\xc3\xa9tat d'avancement", to_field=b'nom', to='ong.avancement'),
        ),
        migrations.AddField(
            model_name='action',
            name='categories',
            field=models.ManyToManyField(to='ong.categorie', verbose_name=b'cat\xc3\xa9gorie'),
        ),
        migrations.AddField(
            model_name='action',
            name='organisme',
            field=models.OneToOneField(verbose_name=b"organisme maitre d'oeuvre", to_field=b'nom', to='ong.organisme'),
        ),
        migrations.AddField(
            model_name='action',
            name='responsable',
            field=models.ForeignKey(to='ong.utilisateur', to_field=b'user', verbose_name=b'nom du responsable de la fiche'),
        ),
    ]
