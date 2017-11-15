# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 05:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20171108_0408'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riff',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
        migrations.AlterField(
            model_name='riff',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='riff_audio/'),
        ),
        migrations.AlterField(
            model_name='riff',
            name='desc',
            field=models.TextField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='riff',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='riff_documents/'),
        ),
        migrations.AlterField(
            model_name='riff',
            name='riff_key',
            field=models.CharField(choices=[('', 'Select'), ('Amaj', 'Amaj'), ('Bmaj', 'Bmaj'), ('Cmaj', 'Cmaj'), ('Dmaj', 'Dmaj'), ('Emaj', 'Emaj'), ('Fmaj', 'Fmaj'), ('Gmaj', 'Gmaj'), ('Abmaj', 'Abmaj'), ('Bbmaj', 'Bbmaj'), ('Dbmaj', 'Dbmaj'), ('Ebmaj', 'Ebmaj'), ('Gbmaj', 'Gbmaj'), ('Amin', 'Amin'), ('Bmin', 'Bmin'), ('Cmin', 'Cmin'), ('Dmin', 'Dmin'), ('Emin', 'Emin'), ('Fmin', 'Fmin'), ('Gmin', 'Gmin'), ('Abmin', 'Abmin'), ('Bbmin', 'Bbmin'), ('Dbmin', 'Dbmin'), ('Ebmin', 'Ebmin'), ('Gbmin', 'Gbmin'), ('Chromatic', 'Chromatic')], default='Select', max_length=20),
        ),
        migrations.AlterField(
            model_name='riff',
            name='tab',
            field=models.TextField(default='G |----|\nD |----|\nA |----|\nE |----|\n', max_length=1000),
        ),
        migrations.AlterField(
            model_name='riff',
            name='tags',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='riff',
            name='timesig_denom',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (4, '4'), (8, '8'), (16, '16'), (32, '32')], default=4),
        ),
    ]