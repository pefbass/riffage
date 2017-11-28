from os.path import basename, splitext
from django.db import models
from django.forms import forms
from riffage.account.models import Profile

class Message(models.Model):

	sender = models.ForeignKey(
		Profile,
		on_delete=models.CASCADE,
		null=True)

	CONTACTS = [
		('', 'Select'),

		# All users go here, once I figure out how to do that.

	]

	recipients = models.CharField(max_length=20, choices=CONTACTS, default='Select', 
		verbose_name='Recipients')

	subject = models.CharField(max_length=50)

	body = models.CharField(max_length=1000)

	read = models.BooleanField(default=False)

	sent_time = models.DateField(auto_now=True, auto_now_add=False)