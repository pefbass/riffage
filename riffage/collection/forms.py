from django.forms import ModelForm, ValidationError
from .models import Riff

class RiffForm(ModelForm):
	class Meta:
		model = Riff
		fields = ['name', 'riff_key', 'timesig_num', 'timesig_denom', 'desc', 'tab', 'tags', 'audio_file']

	def clean(self):
		# get cleaned data
		data = super(RiffForm, self).clean()

		# get tab data from cleaned data, convert from unicode string and remove CR
		tab = str(data.get('tab')).replace('\r', '')
		# get audio data
		audio = data.get('audio')

		# get default value for tab field and remove newlines from the end
		default_tab = Riff._meta.get_field('tab').get_default().strip('\n')

		# if audio doesn't exist and tab doesn't exist or is the default value
		if not audio and (not tab or tab == default_tab):
			raise ValidationError('Must provide either a tab or an audio file')

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if Riff.objects.filter(name=name).exists():
			raise ValidationError('Riff names must be unique')

		return name
