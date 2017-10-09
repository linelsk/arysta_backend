from rest_framework import serializers
from Catalogos.models import (
    categoria,
    subcategoria, 
    Producto, 
    Cultivo,  
    DondeEstamos,
    DondeEstamos_Telefonos
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

class categoriaSerializer(serializers.ModelSerializer):  
        #path = Base64ImageField(required=False)    
        class Meta:
            model = categoria
            fields = ('id', 'nombre')

class subcategoriaSerializer(serializers.ModelSerializer):  
        #path = Base64ImageField(required=False)    
        class Meta:
            model = subcategoria
            fields = ('id', 'id_categoria', 'nombre')

class ProductoSerializer(serializers.ModelSerializer):  
        #path = Base64ImageField(required=False)    
        class Meta:
            model = Producto
            fields = ('id','image', 'nombre', 'definicion' , 'registro', 'formulacion', 'consentracion', 'ingredientes', 'cultivos', 'envases', 'toxitologia', 'expectro', 'categoria', 'subcategoria', 'etiqueta', 'hoja', 'ficha', 'created_by')

class HashedImageSerializer(Serializer):
    image = CharField(required=True)
    extension = CharField(required=True)
    response = ReadOnlyField()

class HashedFileSerializer(Serializer):
    file = CharField(required=True)
    extension = CharField(required=True)
    response = ReadOnlyField()

class CultivoSerializer(serializers.ModelSerializer):  
        #path = Base64ImageField(required=False)    
        class Meta:
            model = Cultivo
            fields = ('id','image', 'definicion' , 'registro', 'cultivo', 'created_by')

class DondeEstamosSerializer(serializers.ModelSerializer):  
        #path = Base64ImageField(required=False)    
        class Meta:
            model = DondeEstamos
            fields = ('id','titulo', 'direccion', 'created_by')

class DondeEstamos_TelefonosSerializer(serializers.ModelSerializer):  
        #path = Base64ImageField(required=False)    
        class Meta:
            model = DondeEstamos_Telefonos
            fields = ('id','image', 'nombre_rtv', 'telefono_rtv', 'movil_rtv', 'mail_rtv', 'nombre_dm', 'telefono_dm', 'movil_dm', 'mail_dm', 'created_by')