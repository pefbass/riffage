from django.forms import ModelForm
from .models import Riff

class NewRiffForm(ModelForm):
	class Meta:
		model = Riff
		fields = ['name']
