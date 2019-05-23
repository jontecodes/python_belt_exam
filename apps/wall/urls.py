######### FOR THE WALLLLLLL #########
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^create_comment/(?P<id>\d+)$', views.create_comment),
    url(r'^like/(?P<id>\d+)$', views.likes),
    url(r'^unlike/(?P<id>\d+)$', views.unlikes),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^destroym/(?P<id>\d+)$', views.destroym),
]