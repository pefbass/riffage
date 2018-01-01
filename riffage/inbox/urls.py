from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^$', inbox, name='inbox'),
	url(r'^message_send/$', message_send, name='message_send'),
	url(r'^message_detail/(?P<pk>\d+)/$', message_detail, name='message_detail'),
	url(r'^message_delete/(?P<pk>\d+)/$', message_delete, name='message_delete'),
]
