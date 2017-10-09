from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
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
    QuienesSomos_acordeon_vision_imagenes,
    QuienesSomos_acordeon_mision,
    QuienesSomos_acordeon_valores,
    Productos,
    Pronutiva,
    Contacto
    ) 

from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField, 
    SerializerMethodField,  
    PrimaryKeyRelatedField, 
    ReadOnlyField, 
    StringRelatedField,
    CharField, 
    ValidationError, 
    EmailField, 
    IntegerField, 
    ImageField, 
    Serializer, 
    BooleanField,  
    DateField, 
    )

UserModel = get_user_model()

class ImageHeaderSerializer(serializers.ModelSerializer):  
        #path = Base64ImageField(required=False)    
        class Meta:
            model = ImageHeader
            fields = ('id','image', 'filename')


class HashedImageSerializer(Serializer):
    image = CharField(required=True)
    extension = CharField(required=True)
    response = ReadOnlyField()
    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'quienessomos', 
            'productos',
            'pronutiva',
            'dondeestamos',
            'contacto',
            'status',
            'created_by',
            'copyright')

class SliderHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderHome
        fields = (
            'id',
            'image', 
            'textomensaje',
            'mensaje_boton',
            'status',
            'created_by')

class Seccion_azul_homeHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion_azul_home
        fields = (
            'id',
            'image', 
            'textomensaje',
            'status',
            'created_by')

class Seccion_video_homeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion_video_home
        fields = (
            'id',
            'video_url', 
            'status',
            'created_by')

class Seccion_distribuidor_homeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion_distribuidor_home
        fields = (
            'id',
            'image',
            'textomensaje', 
            'mensaje_boton',
            'status',
            'created_by')

class Seccion_contacto_homeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion_contacto_home
        fields = (
            'id',
            'image',
            'textomensaje', 
            'mensaje_boton',
            'status',
            'created_by')

class QuienesSomosSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos
        fields = (
            'id',
            'image',
            'textomensaje', 
            'titulo',
            'nosotros',
            'status',
            'created_by')

class QuienesSomos_acordeon_historiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos_acordeon_historia
        fields = (
            'id',
            'image',
            'textomensaje', 
            'status',
            'created_by')

class QuienesSomos_acordeon_mision_imagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos_acordeon_mision_imagenes
        fields = (
            'id',  
            'image',
            'status',
            'created_by')

class QuienesSomos_acordeon_vision_imagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos_acordeon_vision_imagenes
        fields = (
            'id',  
            'image',
            'status',
            'created_by')

class QuienesSomos_acordeon_misionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos_acordeon_mision
        fields = (
            'id',  
            'tiutlo_mision',          
            'mision',
            'tiutlo_vision',
            'vision',
            'status',
            'created_by')

class QuienesSomos_acordeon_valoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienesSomos_acordeon_valores
        fields = (
            'id',
            'image',
            'status',
            'created_by')

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = (
            'id',
            'image',
            'textomensaje',
            'titulo',
            'status',
            'created_by')

class PronutivaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pronutiva
        fields = (
            'id',
            'image',
            'textomensaje',
            'image_titulo',
            'texto_contenido',
            'titulo',
            'status',
            'created_by')


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = (
            'id',
            'image',
            'telefono',
            'correo',
            'localidad',
            'mensaje',
            'mensaje_boton',
            'status',
            'created_by')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username', 'email')
        read_only_fields = ('email', )