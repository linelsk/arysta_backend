# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogos', '0005_auto_20171006_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
