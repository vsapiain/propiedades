from django.conf.urls import include,url
from Api import views

urlpatterns = [
    url(r'^authenticate_user/$', views.authenticate_user, name='authenticate_user'),
    url(r'^verify_token/$', views.verify_token, name='verify_token'),
    url(r'^comunas/$', views.get_communes, name='comunas'),
    url(r'^usuarios/(?P<id>\w+)', views.users, name='users'),
    url(r'^cuentas/(?P<id>\w+)', views.account, name='account'),

]