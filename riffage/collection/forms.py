from django.forms import ModelForm, ValidationError
from .models import Riff

class RiffForm(ModelForm):
	class Meta:
		model = Riff
		fields = ['name', 'riff_key', 'timesig_num', 'timesig_denom', 'desc', 'tab', 'tags', 'audio_file']

	def clean(self):
		data = super(RiffForm, self).clean()

		tab = data.get('tab')
		audio = data.get('audio')

		if not audio and (not tab or tab == u'G |----|\r\nD |----|\r\nA |----|\r\nE |----|'):
			raise ValidationError('Must provide either a tab or an audio file')

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if Riff.objects.filter(name=name).exists():
			raise ValidationError('Riff names must be unique')

		return name
