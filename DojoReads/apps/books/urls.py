from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^homepage$', views.homepage),
    url(r'^login$', views.login),
    url(r'logout$', views.logout),
    url(r'^username$', views.username),
    url(r'^addbook$', views.addbook),
    url(r'^books/add$' , views.addbook),
    url(r'^books/(?P<my_val>\d+)$', views.viewbook),
]


