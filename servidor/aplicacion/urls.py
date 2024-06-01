#from django.conf.urls import url
from django.urls import path
from  . import views



urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('tienda',views.tienda,name='tienda'),
    path('terminos',views.terminos,name='terminos')
]