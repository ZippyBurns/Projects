from django.conf.urls import url
from . import views 

urlpatterns=[
    url(r'^$', views.index),
    url(r'^wall$', views.wall),
    url(r'^login$', views.login),
    url(r'^send_message$', views.send_message),
    url(r'^send_comment$', views.send_comment),
    url(r'logout$', views.logout),
    url(r'delete_message/(?P<id>\d+)$', views.delete_message),
    url(r'delete_comment/(?P<id>\d+)$', views.delete_comment),
]