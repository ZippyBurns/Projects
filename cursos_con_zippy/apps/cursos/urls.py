from django.conf.urls import url
from . import views 

urlpatterns=[
    url(r'^$', views.index),
    url(r'^home$', views.homepage),
    url(r'^login$', views.login),
    url(r'logout$', views.logout),
    url(r'^username$', views.username),
    url(r'^library$', views.library),
    url(r'^greeting', views.greeting),
    url(r'^color', views.color),
    url(r'^number', views.number),
]