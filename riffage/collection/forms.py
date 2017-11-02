from django.forms import ModelForm
from .models import Riff

class RiffForm(ModelForm):
	class Meta:
		model = Riff
		fields = ['name', 'riff_key', 'timesig_num', 'timesig_denom', 'audio_file']
