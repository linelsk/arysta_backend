# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys, base64
from rest_framework.response import Response
from django.shortcuts import render
from django.conf import settings
from rest_framework import generics, permissions, viewsets
from rest_framework.generics import (

    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    CreateAPIView, 
    RetrieveUpdateAPIView 
    )

from AdminManager.models import (
    ImageHeader,
    Menu, 
    SliderHome, 
    Seccion_azul_home,  
    Seccion_video_home,
    Seccion_distribuidor_home,
    Seccion_contacto_home,
    QuienesSomos,
    QuienesSomos_acordeon_historia,
    QuienesSomos_acordeon_mision_imagenes,
    QuienesSomos_acordeon_mision,
    QuienesSomos_acordeon_vision_imagenes,
    QuienesSomos_acordeon_valores,
    Productos,
    Pronutiva,
    Contacto
    ) 

from AdminManager.serializers import (
	ImageHeaderSerializer,
	MenuSerializer,
	SliderHomeSerializer,
	Seccion_azul_homeHomeSerializer,
	Seccion_video_homeSerializer,
	Seccion_distribuidor_homeSerializer,
	Seccion_contacto_homeSerializer,
	QuienesSomosSerializer,
	QuienesSomos_acordeon_historiaSerializer,
    QuienesSomos_acordeon_mision_imagenesSerializer,
	QuienesSomos_acordeon_misionSerializer,
    QuienesSomos_acordeon_vision_imagenesSerializer,
	QuienesSomos_acordeon_valoresSerializer,
	ProductosSerializer,
	PronutivaSerializer,
	ContactoSerializer,
    HashedImageSerializer,
    UserSerializer
    )

from django.contrib.auth.models import User

# views adminfront.

class ImageHeaderList(generics.ListCreateAPIView):
    queryset = ImageHeader.objects.all()
    serializer_class = ImageHeaderSerializer
    permission_classes = [permissions.AllowAny]

class ImageHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageHeader.objects.all()
    serializer_class = ImageHeaderSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImage(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        path = os.path.join(settings.MEDIA_ROOT, 'imagen_menu', 'arysta_logo' + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "imagen_menu/arysta_logo", 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.AllowAny]

class SliderHomeList(generics.ListCreateAPIView):
    queryset = SliderHome.objects.all()
    serializer_class = SliderHomeSerializer
    permission_classes = [permissions.AllowAny]

class SliderHomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SliderHome.objects.all()
    serializer_class = SliderHomeSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageSlider(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'imagen_slider', filename + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "imagen_slider/" + filename, 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class Seccion_azul_homeList(generics.ListCreateAPIView):
    queryset = Seccion_azul_home.objects.all()
    serializer_class = Seccion_azul_homeHomeSerializer
    permission_classes = [permissions.AllowAny]

class Seccion_azul_homeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seccion_azul_home.objects.all()
    serializer_class = Seccion_azul_homeHomeSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageAzul(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        #filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'seccion_azul', 'seccion_azul' + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "seccion_azul/" + 'seccion_azul', 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class Seccion_video_homeList(generics.ListCreateAPIView):
    queryset = Seccion_video_home.objects.all()
    serializer_class = Seccion_video_homeSerializer
    permission_classes = [permissions.AllowAny]

class Seccion_video_homeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seccion_video_home.objects.all()
    serializer_class = Seccion_video_homeSerializer
    permission_classes = [permissions.AllowAny]

class Seccion_distribuidor_homeList(generics.ListCreateAPIView):
    queryset = Seccion_distribuidor_home.objects.all()
    serializer_class = Seccion_distribuidor_homeSerializer
    permission_classes = [permissions.AllowAny]

class Seccion_distribuidor_homeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seccion_distribuidor_home.objects.all()
    serializer_class = Seccion_distribuidor_homeSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageDistribuidor(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        #filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'seccion_distribuidor', 'seccion_distribuidor' + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "seccion_distribuidor/" + 'seccion_distribuidor', 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class Seccion_contacto_homeList(generics.ListCreateAPIView):
    queryset = Seccion_contacto_home.objects.all()
    serializer_class = Seccion_contacto_homeSerializer
    permission_classes = [permissions.AllowAny]

class Seccion_contacto_homeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seccion_contacto_home.objects.all()
    serializer_class = Seccion_contacto_homeSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageContacto(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        #filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'seccion_contacto', 'seccion_contacto' + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "seccion_contacto/" + 'seccion_contacto', 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class QuienesSomosList(generics.ListCreateAPIView):
    queryset = QuienesSomos.objects.all()
    serializer_class = QuienesSomosSerializer
    permission_classes = [permissions.AllowAny]

class QuienesSomosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuienesSomos.objects.all()
    serializer_class = QuienesSomosSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageQuienesSomos(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        #filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'quienessomos', 'quienessomos_img' + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "quienessomos/" + 'quienessomos_img', 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class QuienesSomos_acordeon_historiaList(generics.ListCreateAPIView):
    queryset = QuienesSomos_acordeon_historia.objects.all()
    serializer_class = QuienesSomos_acordeon_historiaSerializer
    permission_classes = [permissions.AllowAny]

class QuienesSomos_acordeon_historiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuienesSomos_acordeon_historia.objects.all()
    serializer_class = QuienesSomos_acordeon_historiaSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageAcordeonHistoria(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        #filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'acordeonhistoria', 'acordeonhistoria' + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "acordeonhistoria/" + 'acordeonhistoria', 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class QuienesSomos_acordeon_misionList(generics.ListCreateAPIView):
    queryset = QuienesSomos_acordeon_mision.objects.all()
    serializer_class = QuienesSomos_acordeon_misionSerializer
    permission_classes = [permissions.AllowAny]

class QuienesSomos_acordeon_misionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuienesSomos_acordeon_mision.objects.all()
    serializer_class = QuienesSomos_acordeon_misionSerializer
    permission_classes = [permissions.AllowAny]

##Mision
class QuienesSomos_acordeon_mision_imagenesList(generics.ListCreateAPIView):
    queryset = QuienesSomos_acordeon_mision_imagenes.objects.all()
    serializer_class = QuienesSomos_acordeon_mision_imagenesSerializer
    permission_classes = [permissions.AllowAny]

class QuienesSomos_acordeon_mision_imagenesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuienesSomos_acordeon_mision_imagenes.objects.all()
    serializer_class = QuienesSomos_acordeon_mision_imagenesSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageMisionImagen(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'mision', filename + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "mision/" + filename, 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

##Vision
class QuienesSomos_acordeon_vision_imagenesList(generics.ListCreateAPIView):
    queryset = QuienesSomos_acordeon_vision_imagenes.objects.all()
    serializer_class = QuienesSomos_acordeon_vision_imagenesSerializer
    permission_classes = [permissions.AllowAny]

class QuienesSomos_acordeon_vision_imagenesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuienesSomos_acordeon_vision_imagenes.objects.all()
    serializer_class = QuienesSomos_acordeon_vision_imagenesSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageVisionImagen(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'vision', filename + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "vision/" + filename, 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class QuienesSomos_acordeon_valoresList(generics.ListCreateAPIView):
    queryset = QuienesSomos_acordeon_valores.objects.all()
    serializer_class = QuienesSomos_acordeon_valoresSerializer
    permission_classes = [permissions.AllowAny]

class QuienesSomos_acordeon_valoresDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuienesSomos_acordeon_valores.objects.all()
    serializer_class = QuienesSomos_acordeon_valoresSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImagevalores(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'valores', filename + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "valores/" + filename, 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class ProductosList(generics.ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.AllowAny]

class ProductosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [permissions.AllowAny]

class HeaderUpdateImageSliderProductos(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        #filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'slider_producto', "slider_producto" + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "slider_producto/" + "slider_producto", 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class PronutivaList(generics.ListCreateAPIView):
    queryset = Pronutiva.objects.all()
    serializer_class = PronutivaSerializer
    permission_classes = [permissions.AllowAny]

class PronutivaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pronutiva.objects.all()
    serializer_class = PronutivaSerializer
    permission_classes = [permissions.AllowAny]

class ContactoList(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    permission_classes = [permissions.AllowAny]

class ContactoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    permission_classes = [permissions.AllowAny]
    
class CurrentUserList(generics.ListCreateAPIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    

