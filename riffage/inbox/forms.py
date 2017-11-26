from django.forms import ModelForm, ValidationError
from os.path import splitext
from .models import Message

class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = ['recipients', 'subject', 'body']

	def __init__(self, *args, **kwargs):
		super(MessageForm, self).__init__(*args, **kwargs)