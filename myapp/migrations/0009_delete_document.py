# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-07 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
