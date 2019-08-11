from django.conf.urls import include,url
from PropiedadesApp import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^SetUser/', views.actualizar_usuario, name='SetUser'),
    url(r'^SetAccount/', views.actualizar_cuenta, name='SetAccount'),
    url(r'^usuarios/info', views.obtener_usuario, name='obtener_usuario'),
    url(r'^GetPlans', views.obtener_planes, name='obtener_planes'),
    url(r'^publicar/', views.publicar_propiedad, name='publicar_propiedad'),
    url(r'^SetProperty/', views.publicar_propiedad, name='publicar_propiedad'),
]