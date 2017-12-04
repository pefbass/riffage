from django.test import TestCase

# Create your tests here.
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.test import TestCase
from riffage.account.models import Profile, PasswordResetForm
from django.contrib.auth.models import User
from .forms import MessageForm
from .models import Message

# Create your tests here.

class TestInboxApp(TestCase):
	
	def test_send_message_page(self):
		msg_found = False
		msg = Message(
			message_sent_by="test_user_1", 
			message_received_by="test_user_2",
			subject="Test",
			body="Test")

		msg.save()
		
		messages = Message.objects.all()

		for message in messages:
			if (message.subject == "Test" and message.body == "Test" and message.message_sent_by == "test_user_1"):
				msg_found = True

		self.assertTrue(msg_found)
	
	def test_receive_message_page(self):
		msg_found = False
		msg = Message(message_sent_by="test_user_1", 
			message_received_by="test_user_2",
			subject="Test",
			body="Test")

		msg.save()

		messages = Message.objects.all()

		for message in messages:
			if (message.subject == "Test" and message.body == "Test" and message.message_received_by == "test_user_2"):
				msg_found = True

		self.assertTrue(msg_found)

