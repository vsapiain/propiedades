from django.conf.urls import include,url
from Api import views

urlpatterns = [
    url(r'^usuarios/$', views.user_list, name='user_list')
]