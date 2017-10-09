# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Modelos Index.
class ImageHeader(models.Model):
    image = models.CharField(max_length=500, blank=True)
    filename =  models.CharField(max_length=200, blank=True)  

    def __unicode__(self):
		return self.filename

class Menu(models.Model):
	quienessomos = models.CharField(max_length=200, blank=True)
	productos = models.CharField(max_length=200, blank=True)
	pronutiva = models.CharField(max_length=200, blank=True)
	dondeestamos = models.CharField(max_length=200, blank=True)
	contacto = models.CharField(max_length=200, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)
	copyright = models.CharField(max_length=700, blank=True)

	def __unicode__(self):
		return self.quienessomos

class SliderHome(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=2000, blank=True)
	mensaje_boton = models.CharField(max_length=100, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.mensaje_boton

class Seccion_azul_home(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=2000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=True, blank=True)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje

class Seccion_video_home(models.Model):
	video_url = models.CharField(max_length=500, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.video_url

class Seccion_distribuidor_home(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=2000, blank=True)
	mensaje_boton = models.CharField(max_length=100, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje

class Seccion_contacto_home(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=2000, blank=True)
	mensaje_boton = models.CharField(max_length=100, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje

class QuienesSomos(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=2000, blank=True)
	titulo = models.CharField(max_length=200, blank=True)
	nosotros = models.CharField(max_length=500000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje

class QuienesSomos_acordeon_historia(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=5000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje

class QuienesSomos_acordeon_mision(models.Model):
	# image_entrega = models.CharField(max_length=500, blank=True)
	# image_disciplina = models.CharField(max_length=500, blank=True)
	# image_responsables = models.CharField(max_length=500, blank=True)
	tiutlo_mision = models.CharField(max_length=200, blank=True)
	mision = models.CharField(max_length=5000, blank=True)
	# image_clientes= models.CharField(max_length=500, blank=True)
	# image_comunidad = models.CharField(max_length=500, blank=True)
	# image_empleados = models.CharField(max_length=500, blank=True)
	# image_accionistas = models.CharField(max_length=500, blank=True)
	tiutlo_vision = models.CharField(max_length=200, blank=True)
	vision = models.CharField(max_length=500, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.mision

class QuienesSomos_acordeon_mision_imagenes(models.Model):
	image = models.CharField(max_length=500, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.image

class QuienesSomos_acordeon_vision_imagenes(models.Model):	
	image = models.CharField(max_length=500, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.image

class QuienesSomos_acordeon_valores(models.Model):
	image = models.CharField(max_length=500, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.status

class Productos(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=5000, blank=True)
	titulo = models.CharField(max_length=1000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.status

class Pronutiva(models.Model):
	image = models.CharField(max_length=500, blank=True)
	textomensaje = models.CharField(max_length=5000, blank=True)
	image_titulo = models.CharField(max_length=500, blank=True)
	texto_contenido = models.CharField(max_length=5000, blank=True)
	titulo = models.CharField(max_length=1000, blank=True)
	status = models.BooleanField(null=False, default=True)
	created_by = models.IntegerField('auth.User', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.IntegerField('auth.User', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
		return self.textomensaje

class Contacto(models.Model):
	image = models.CharField(max_length=500, blank=True)
	nombres = models.CharField(max_length=800, null=True, blank=True)
	telefono = models.CharField(max_length=100, null=True, blank=True)
	correo = models.CharField(max_length=300, null=True, blank=True)
	localidad = models.CharField(max_length=300, null=True, blank=True)
	mensaje = models.CharField(max_length=5000, null=True, blank=True)
	mensaje_boton = models.CharField(max_length=300, null=True, blank=True)
	created_by = models.ForeignKey('auth.User', related_name='ContactanosCreate', null=False)
	creation_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	modified_by = models.ForeignKey('auth.User', related_name='ContactanosModified', null=True, blank=True)
	modification_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self):
			return self.nombres