from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^$', collection),
	url(r'^riff_new/$', riff_new),
	url(r'^riff/(?P<pk>\d+)/$', riff_detail, name='riff_detail'),
	url(r'^riff_edit/(?P<pk>\d+)/$', riff_edit, name = 'riff_edit'),
	url(r'^logout$', logout, name = 'logout'),
]
