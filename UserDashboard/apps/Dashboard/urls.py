from django.conf.urls import url
from . import views 

urlpatterns=[
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'logout$', views.logout),
    url(r'^username$', views.username),
    url(r'^admin$', views.admin),
    url(r'^adduser$', views.adduser),
    url(r'^profile/(?P<my_val>\d+)$', views.profile),
    url(r'^send_message/(?P<my_val>\d+)$', views.send_message),
    url(r'^send_comment/(?P<my_val>\d+)$', views.send_comment),
    url(r'^delete_message/(?P<my_val>\d+)$', views.delete_message),
    url(r'^delete_comment/(?P<my_val>\d+)$', views.delete_comment),
]