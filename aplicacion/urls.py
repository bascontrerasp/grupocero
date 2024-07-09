#from django.conf.urls import url
from django.urls import path,include
from  . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views



urlpatterns = [
    ## URLS PÁGINA
    path('base', views.base, name='base'),
    path('admin_site',views.admin_site,name='admin_site'),
    path('', views.index, name='index'),
    path('formulario', views.formulario, name='formulario'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('tienda',views.tienda,name='tienda'),
    path('terminos',views.terminos,name='terminos'),
    path('monalisa',views.monalisa,name='monalisa'),
    path('demoiselles',views.demoiselles,name='demoiselles'),
    path('clocks',views.clocks,name='clocks'),
    path('perfil',views.perfil,name='perfil'),

    ## URLS CRUD
    path('crud',views.crud,name='crud'),
    path('cliente_del/<str:pk>',views.cliente_del,name='cliente_del'),
    path('cliente_findEdit/<str:pk>',views.cliente_findEdit,name='cliente_findEdit'),
    path('editar',views.editar,name='editar'),
    path('cliente_add',views.cliente_add,name='cliente_add'),
    path('logeo',views.logeo,name='logeo'),
    path('logout', views.logout, name='logout'),
    path('cliente_update',views.cliente_update,name='cliente_update'),

    ## URLS FORM
    path('crud_ciudades',views.crud_ciudades,name='crud_ciudades'),
    path('ciudades_add',views.ciudades_add,name='ciudades_add'),
    path('ciudades_del/<str:pk>',views.ciudades_del,name='ciudades_del'),
    path('ciudades_edit/<str:pk>',views.ciudades_edit,name='ciudades_edit'),

    ## URL ADMIN
    path('admin_site',views.admin_site,name="admin_site"),
    path('login',views.login,name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('acceso_denegado', views.acceso_denegado, name='acceso_denegado'),
]