from django.conf.urls import include,url
from PropiedadesApp import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^comunas/', views.obtener_comunas, name='obtener_comunas'),
    url(r'^usuarios/info', views.obtener_usuario, name='obtener_usuario'),
]