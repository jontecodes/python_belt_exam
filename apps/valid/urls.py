######### FOR THE WALLLLLLL #########
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^show/$', views.show),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quotes$', views.quotes),
    url(r'^add-quote$', views.add_quote),
    url(r'^delete-quote$', views.del_quote),
    url(r'^user/(?P<quote_id>\d+)$', views.user_quotes),
    url(r'^myaccount/(?P<acc_id>\d+)$', views.edit_user),
    url(r'^like/(?P<q_id>\d+)$', views.like_quote),
    url(r'^update-user$', views.update_user)
    
]