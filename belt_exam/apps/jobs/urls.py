from django.conf.urls import url
from . import views 

urlpatterns=[
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'logout$', views.logout),
    url(r'addJob$', views.addJob),
    url(r'view/(?P<id>\d+)$', views.view),
    url(r'edit/(?P<id>\d+)$' , views.edit),
    url(r'add/(?P<id>\d+)$' , views.addlist),
    url(r'delete/(?P<id>\d+)$' , views.delete),
    url(r'logout$', views.logout),
]