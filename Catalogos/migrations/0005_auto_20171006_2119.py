# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 21:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogos', '0004_subcategoria_id_catgoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategoria',
            old_name='id_catgoria',
            new_name='id_categoria',
        ),
    ]
