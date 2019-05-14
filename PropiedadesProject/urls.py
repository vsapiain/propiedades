"""PropiedadesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from PropiedadesApp import views
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^propiedades/$', views.propiedades, name='propiedades'),
    url(r'^propiedades/(?P<propiedad_codigo>\w+)', views.detalle, name='detalle'),
    url(r'^planes/', views.planes, name='planes'),
    url(r'^usuarios/generales/editar', views.editar_usuario, name='editar_usuario'),
    url(r'^usuarios/cuentas/editar', views.editar_cuenta, name='editar_cuenta'),
    url(r'^verificar_usuario/', views.verificar_usuario, name='verificar_usuario'),
    url(r'^api/', include('Api.urls')),
    url(r'', include('PropiedadesApp.urls')),
    #url(r'^login/', views.login, name='login'),
    #url(r'^usuarios/get', views.obtener_usuario, name='obtener_usuario'),
    #url(r'^admin/', admin.site.urls),
]
