from django.urls import path, include
from .views import *  
from django.contrib.auth.views import LogoutView              #Para importar todo de views en la misma carpeta

urlpatterns = [
    path('',inicio, name='inicio'),
    path('registrate/',registrate, name='registrate'),
    path('vender/', vender, name='vender'),
    path('comprar/',comprar, name='comprar'),
    path('acercademi/', acercaDeMi, name="acercaDeMi"),



#catalogos
    #path('catalogo/',catalogo, name='catalogo'),
    path('catalogo_oleos/',OleoList.as_view(), name="oleos"),
    path('catalogo_acuarelas/',AcuarelaList.as_view(), name="acuarela"),
    path('catalogo_carboncillos/',CarboncilloList.as_view(), name="carboncillo"),


    
#buscadores
    path('buscarOleo/', buscarOleo, name='buscarOleo'),
    path('buscar2/', buscar2, name='buscar2'),

    path('buscarAcuarela/', buscarAcuarela, name='buscarAcuarela'),
    path('buscar3/', buscar3, name='buscar3'),

    path('buscarCarboncillo/', buscarCarboncillo, name='buscarCarboncillo'),
    path('buscar4/', buscar4, name='buscar4'),




#inicio de sesion
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="app/logout.html"), name='logout'),
    path('registro/', registrar, name="registro" ),
    path('editarUsuario/', editarUsuario, name="editarUsuario" ),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar" ),



#registrar productos
    path('crear_oleo/', OleoCrear.as_view(), name="crear_oleo" ),
    path('crear_acuarela/', AcuarelaCrear.as_view(), name="crear_acuarela" ),
    path('crear_carboncillo/', CarboncilloCrear.as_view(), name="crear_carboncillo" ),

#editar productos
path('editar_oleo/<int:pk>/', OleoEditar.as_view(), name="editar_oleo" ),
path('editar_acuarela/<int:pk>/', AcuarelaEditar.as_view(), name="editar_acuarela" ),
path('editar_carboncillo/<int:pk>/', CarboncilloEditar.as_view(), name="editar_carboncillo" ),

#borrar productos
 path('borrar_oleo/<int:pk>/', OleoBorrar.as_view(), name="borrar_oleo" ),
 path('borrar_acuarela/<int:pk>/', AcuarelaBorrar.as_view(), name="borrar_acuarela" ),
 path('borrar_carboncillo/<int:pk>/', CarboncilloBorrar.as_view(), name="borrar_carboncillo" ),


    ]