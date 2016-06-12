from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^player/$', views.player, name='player'),
    url(r'^transfer/$', views.transfer, name='transfer'),
    url(r'^team/$', views.team, name='team'),
]