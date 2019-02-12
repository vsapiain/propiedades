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
    url(r'^propiedades/detalle/(?P<propiedad_codigo>\w+)', views.detalle, name='detalle'),
    url(r'^login/', views.login, name='login'),
    url(r'^planes/', views.planes, name='planes'),
    url(r'^api/', include('Api.urls'))
    #url(r'^admin/', admin.site.urls),
]
