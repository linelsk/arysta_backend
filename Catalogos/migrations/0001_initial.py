# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-26 22:52
from __future__ import unicode_literals

import Catalogos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=200)),
                ('definicion', models.CharField(blank=True, max_length=1000)),
                ('registro', models.CharField(blank=True, max_length=1000)),
                ('cultivo', models.CharField(blank=True, max_length=1000)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(verbose_name='auth.User')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.IntegerField(blank=True, null=True, verbose_name='auth.User')),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DondeEstamos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=1000)),
                ('direccion', models.CharField(blank=True, max_length=1000)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(verbose_name='auth.User')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.IntegerField(blank=True, null=True, verbose_name='auth.User')),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DondeEstamos_Telefonos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=500)),
                ('nombre_rtv', models.CharField(blank=True, max_length=1000)),
                ('telefono_rtv', models.CharField(blank=True, max_length=1000)),
                ('movil_rtv', models.CharField(blank=True, max_length=1000)),
                ('mail_rtv', models.CharField(blank=True, max_length=1000)),
                ('nombre_dm', models.CharField(blank=True, max_length=1000)),
                ('telefono_dm', models.CharField(blank=True, max_length=1000)),
                ('movil_dm', models.CharField(blank=True, max_length=1000)),
                ('mail_dm', models.CharField(blank=True, max_length=1000)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(verbose_name='auth.User')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.IntegerField(blank=True, null=True, verbose_name='auth.User')),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=200)),
                ('definicion', models.CharField(blank=True, max_length=1000)),
                ('registro', models.CharField(blank=True, max_length=1000)),
                ('formulacion', models.CharField(blank=True, max_length=1000)),
                ('consentracion', models.CharField(blank=True, max_length=1000)),
                ('ingredientes', models.CharField(blank=True, max_length=1000)),
                ('cultivos', models.CharField(blank=True, max_length=1000)),
                ('envases', models.CharField(blank=True, max_length=1000)),
                ('toxitologia', models.CharField(blank=True, max_length=1000)),
                ('expectro', models.CharField(blank=True, max_length=1000)),
                ('categoria', models.IntegerField(verbose_name=Catalogos.models.categoria)),
                ('subcategoria', models.IntegerField(verbose_name=Catalogos.models.subcategoria)),
                ('etiqueta', models.CharField(blank=True, max_length=200)),
                ('hoja', models.CharField(blank=True, max_length=200)),
                ('ficha', models.CharField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(verbose_name='auth.User')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.IntegerField(blank=True, null=True, verbose_name='auth.User')),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='subcategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]