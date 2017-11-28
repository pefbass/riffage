# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_message_recipients'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message_received_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='message_sent_by',
            field=models.IntegerField(null=True),
        ),
    ]
