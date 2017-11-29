from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^$', inbox, name='inbox'),
	url(r'^send_message/$', send_message, name='send_message'),
	url(r'^message_detail/(?P<pk>\d+)/$', message_detail, name='message_detail')
]
