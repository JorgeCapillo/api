
from django.conf.urls import include, url
from django.contrib import admin
from app.views import *
from usuarios.views import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuarios/$',usuarios,name="usuarios"),
    url(r'^usuarios/crear',crearUser),
    url(r'^usuarios/eliminar/$',eliminarUser),
    url(r'^$',home,name="home"),
    url(r'^usuarios/salir',salir,name="salir"),
    url(r'^usuarios/login',login),
]
