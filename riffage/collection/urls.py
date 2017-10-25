from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^$', index),
	url(r'^newriff/$', new_riff),
	url(r'^riff/(?P<pk>\d+)/$', riff_detail, name='riff_detail'),
]
