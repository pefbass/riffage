from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^$', inbox, name='inbox'),
	url(r'^send_message/$', send_message, name='send_message'),
]
