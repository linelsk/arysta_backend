# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os, sys, base64
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets

from rest_framework.generics import (

    ListAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    CreateAPIView, 
    RetrieveUpdateAPIView, 
    )

from Catalogos.models import (
    categoria,
    subcategoria, 
    Producto, 
    Cultivo,  
    DondeEstamos,
    DondeEstamos_Telefonos
    ) 

from Catalogos.serializers import (
	categoriaSerializer,
	subcategoriaSerializer,
	ProductoSerializer,
	CultivoSerializer,
	DondeEstamosSerializer,
	DondeEstamos_TelefonosSerializer,
    HashedImageSerializer,
    HashedFileSerializer
    )

# Create your views here.
class categoriaList(generics.ListCreateAPIView):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer
    permission_classes = [permissions.AllowAny]

class categoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = categoria.objects.all()
    serializer_class = categoriaSerializer
    permission_classes = [permissions.AllowAny]

class subcategoriaList(generics.ListCreateAPIView):
    queryset = subcategoria.objects.all()
    serializer_class = subcategoriaSerializer
    permission_classes = [permissions.AllowAny]

class subcategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = subcategoria.objects.all()
    serializer_class = subcategoriaSerializer
    permission_classes = [permissions.AllowAny]

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]

class UpdateImageProductos(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'productos', filename + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "productos/" + filename, 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class UpdateFileArchivosProductos(RetrieveUpdateAPIView):
    serializer_class = HashedFileSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        file = self.request.data.get("file")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'achivos_producto', filename + '.' + extension)
        f = open(path, "w+b")
        f.write(file.decode('base64')) 
        f.close()
        response = { 'file': "achivos_producto/" + filename, 'extension': extension, 'response':  "success", }
        serializer = HashedFileSerializer(response)
        return Response(serializer.data)


class CultivoList(generics.ListCreateAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
    permission_classes = [permissions.AllowAny]

class CultivoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
    permission_classes = [permissions.AllowAny]

class UpdateImageCultivo(RetrieveUpdateAPIView):
    serializer_class = HashedImageSerializer
    permission_classes = [permissions.AllowAny]

    def update(self, serializer):
        image = self.request.data.get("image")
        extension = self.request.data.get("extension")
        #decoded = base64.b64decode(image)
        filename = self.request.data.get("filename")
        path = os.path.join(settings.MEDIA_ROOT, 'cultivos', filename + '.' + extension)
        f = open(path, "w+b")
        f.write(image.decode('base64')) 
        f.close()
        response = { 'image': "cultivos/" + filename, 'extension': extension, 'response':  "success", }
        serializer = HashedImageSerializer(response)
        return Response(serializer.data)

class DondeEstamosList(generics.ListCreateAPIView):
    queryset = DondeEstamos.objects.all()
    serializer_class = DondeEstamosSerializer
    permission_classes = [permissions.AllowAny]

class DondeEstamosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DondeEstamos.objects.all()
    serializer_class = DondeEstamosSerializer
    permission_classes = [permissions.AllowAny]

class DondeEstamos_TelefonosList(generics.ListCreateAPIView):
    queryset = DondeEstamos_Telefonos.objects.all()
    serializer_class = DondeEstamos_TelefonosSerializer
    permission_classes = [permissions.AllowAny]

class DondeEstamos_TelefonosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DondeEstamos_Telefonos.objects.all()
    serializer_class = DondeEstamos_TelefonosSerializer
    permission_classes = [permissions.AllowAny]