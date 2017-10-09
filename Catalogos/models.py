# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Catalogos.

class categoria(models.Model):
	nombre = models.CharField(max_length=1000, blank=True)

	def __unicode__(self):
		return self.nombre
		

class subcategoria(models.Model):
	id_categoria = models.IntegerField(categoria, null=False)
	nombre = models.CharField(max_length=1000, blank=True)

	def __unicode__(self):
		return self.nombre


class Cultivo(models.Model):
	image = models.ImageField(max_length=200, blank=True)
	definicion = models.CharField(max_length=1000, blank=True)
	registro = models.CharField(max_length=1000, blank=True)
	cultivo = models.CharField(max_length=1000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.definicion

class Producto(models.Model):
	image = models.CharField(max_length=200, blank=True)
	nombre = models.CharField(max_length=1000, blank=True)
	definicion = models.CharField(max_length=1000, blank=True)
	registro = models.CharField(max_length=1000, blank=True)
	formulacion = models.CharField(max_length=1000, blank=True)
	consentracion = models.CharField(max_length=1000, blank=True)
	ingredientes = models.CharField(max_length=1000, blank=True)
	cultivos = models.ManyToManyField(Cultivo, blank=True, related_name="productocultivo")
	envases = models.CharField(max_length=1000, blank=True)
	toxitologia = models.CharField(max_length=1000, blank=True)
	expectro = models.CharField(max_length=1000, blank=True)
	categoria = models.ManyToManyField(categoria, blank=True, related_name="productocategoria")
	subcategoria = models.ManyToManyField(subcategoria, blank=True, related_name="productosubcategoria")
	etiqueta = models.CharField(max_length=200, blank=True)
	hoja = models.CharField(max_length=200, blank=True)
	ficha = models.CharField(max_length=200, blank=True)	
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.definicion

class DondeEstamos(models.Model):
	titulo = models.CharField(max_length=1000, blank=True)
	direccion = models.CharField(max_length=1000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje

class DondeEstamos_Telefonos(models.Model):
	image = models.CharField(max_length=500, blank=True)
	nombre_rtv = models.CharField(max_length=1000, blank=True)
	telefono_rtv = models.CharField(max_length=1000, blank=True)
	movil_rtv = models.CharField(max_length=1000, blank=True)
	mail_rtv = models.CharField(max_length=1000, blank=True)
	nombre_dm = models.CharField(max_length=1000, blank=True)
	telefono_dm = models.CharField(max_length=1000, blank=True)
	movil_dm = models.CharField(max_length=1000, blank=True)
	mail_dm = models.CharField(max_length=1000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje
