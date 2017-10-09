from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from AdminManager import views

urlpatterns = [
   url(r'^ImagenHeader/$', views.ImageHeaderList.as_view()),
   url(r'^ImagenHeaderUpdate/(?P<pk>[0-9]+)/$', views.ImageHeaderDetail.as_view()),
   url(r'^SubirImagenHeader/$', views.HeaderUpdateImage.as_view(), name='logo'),

   url(r'^Menu/$', views.MenuList.as_view()),
   url(r'^MenuUpdate/(?P<pk>[0-9]+)/$', views.MenuDetail.as_view()),

   url(r'^Slider/$', views.SliderHomeList.as_view()),
   url(r'^SliderUpdate/(?P<pk>[0-9]+)/$', views.SliderHomeDetail.as_view()),   
   url(r'^SubirImagenSlider/$', views.HeaderUpdateImageSlider.as_view(), name='slider'),
   
   url(r'^Seccion_azul/$', views.Seccion_azul_homeList.as_view()),
   url(r'^Seccion_azulUpdate/(?P<pk>[0-9]+)/$', views.Seccion_azul_homeDetail.as_view()),
   url(r'^SubirImagenseccionAzul/$', views.HeaderUpdateImageAzul.as_view(), name='azul'),

   url(r'^Seccion_video/$', views.Seccion_video_homeList.as_view()),
   url(r'^Seccion_videoUpdate/(?P<pk>[0-9]+)/$', views.Seccion_video_homeDetail.as_view()) ,  

   url(r'^Seccion_distribuidor/$', views.Seccion_distribuidor_homeList.as_view()),
   url(r'^Seccion_distribuidorUpdate/(?P<pk>[0-9]+)/$', views.Seccion_distribuidor_homeDetail.as_view()),
   url(r'^SubirImagenseccionDistribuidor/$', views.HeaderUpdateImageDistribuidor.as_view(), name='azul'),

   url(r'^Seccion_contacto/$', views.Seccion_contacto_homeList.as_view()),
   url(r'^Seccion_contactoUpdate/(?P<pk>[0-9]+)/$', views.Seccion_contacto_homeDetail.as_view()),
   url(r'^SubirImagenseccionContacto/$', views.HeaderUpdateImageContacto.as_view(), name='azul'),

   url(r'^QuienesSomos/$', views.QuienesSomosList.as_view()),
   url(r'^QuienesSomosUpdate/(?P<pk>[0-9]+)/$', views.QuienesSomosDetail.as_view()),
   url(r'^SubirImagenquienessomos/$', views.HeaderUpdateImageQuienesSomos.as_view(), name='azul'),

   url(r'^Acordeon_historia/$', views.QuienesSomos_acordeon_historiaList.as_view()),
   url(r'^Acordeon_historiaUpdate/(?P<pk>[0-9]+)/$', views.QuienesSomos_acordeon_historiaDetail.as_view()),
   url(r'^SubirImagenAcordeonHistoria/$', views.HeaderUpdateImageAcordeonHistoria.as_view(), name='azul'),

   url(r'^Acordeon_mision/$', views.QuienesSomos_acordeon_misionList.as_view()),
   url(r'^Acordeon_misionUpdate/(?P<pk>[0-9]+)/$', views.QuienesSomos_acordeon_misionDetail.as_view()),
      
   url(r'^Acordeon_mision_imagen/$', views.QuienesSomos_acordeon_mision_imagenesList.as_view()),
   url(r'^Acordeon_mision_imagenUpdate/(?P<pk>[0-9]+)/$', views.QuienesSomos_acordeon_mision_imagenesDetail.as_view()),
   url(r'^SubirImagenAcordeonMision/$', views.HeaderUpdateImageMisionImagen.as_view(), name='azul'),

   url(r'^Acordeon_vision_imagen/$', views.QuienesSomos_acordeon_vision_imagenesList.as_view()),
   url(r'^Acordeon_vision_imagenUpdate/(?P<pk>[0-9]+)/$', views.QuienesSomos_acordeon_vision_imagenesDetail.as_view()),
   url(r'^SubirImagenAcordeonVision/$', views.HeaderUpdateImageVisionImagen.as_view(), name='azul'),

   url(r'^Acordeon_valores/$', views.QuienesSomos_acordeon_valoresList.as_view()),
   url(r'^Acordeon_valoresUpdate/(?P<pk>[0-9]+)/$', views.QuienesSomos_acordeon_valoresDetail.as_view()),
   url(r'^SubirImagenAcordeonValores/$', views.HeaderUpdateImagevalores.as_view(), name='azul'),
   
   url(r'^Productos/$', views.ProductosList.as_view()),
   url(r'^ProductosUpdate/(?P<pk>[0-9]+)/$', views.ProductosDetail.as_view()), 
   url(r'^SubirImagenSliderProducto/$', views.HeaderUpdateImageSliderProductos.as_view(), name='azul'),

   url(r'^Pronutiva/$', views.PronutivaList.as_view()),
   url(r'^PronutivaUpdate/(?P<pk>[0-9]+)/$', views.PronutivaDetail.as_view()),

   url(r'^Contacto$', views.ContactoList.as_view()),
   url(r'^ContactoUpdate/(?P<pk>[0-9]+)/$', views.ContactoDetail.as_view()),

   url(r'^UserCurrent/$', views.CurrentUserList.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)