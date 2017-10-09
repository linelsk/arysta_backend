from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from Catalogos import views

urlpatterns = [

   url(r'^Categoria/$', views.categoriaList.as_view()),
   url(r'^CategoriaUpdate/(?P<pk>[0-9]+)/$', views.categoriaDetail.as_view()),

   url(r'^SubCategoria/$', views.subcategoriaList.as_view()),
   url(r'^SubCategoriaUpdate/(?P<pk>[0-9]+)/$', views.subcategoriaDetail.as_view()),

   url(r'^Producto/$', views.ProductoList.as_view()),
   url(r'^ProductoUpdate/(?P<pk>[0-9]+)/$', views.ProductoDetail.as_view()),
   url(r'^SubirImagenProductos/$', views.UpdateImageProductos.as_view(), name='azul'),
   url(r'^SubirArchivoProductos/$', views.UpdateFileArchivosProductos.as_view(), name='azul'),

   url(r'^Cultivo/$', views.CultivoList.as_view()),
   url(r'^CultivoUpdate/(?P<pk>[0-9]+)/$', views.CultivoDetail.as_view()),
   url(r'^SubirImagenCultivo/$', views.UpdateImageCultivo.as_view(), name='azul'),

   url(r'^DondeEstamos/$', views.DondeEstamosList.as_view()),
   url(r'^DondeEstamosUpdate/(?P<pk>[0-9]+)/$', views.DondeEstamosDetail.as_view()),

   url(r'^DondeEstamos_telefono/$', views.DondeEstamos_TelefonosList.as_view()),
   url(r'^DondeEstamos_telefonoUpdate/(?P<pk>[0-9]+)/$', views.DondeEstamos_TelefonosDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)