from django.forms import ModelForm, ValidationError
from os.path import splitext
from .models import Riff
from riffage.collection.custom import SeparatedValuesField


class RiffForm(ModelForm):
	class Meta:
		model = Riff
		fields = ['name', 'priv_vis', 'riff_key', 'timesig_num', 'timesig_denom', 'desc', 'tab', 'tags', 'audio_file', 'document']
	
	def __init__(self, *args, **kwargs):
		# set edit=True if this form is editing a riff model rather than creating one
		self.edit = kwargs.pop('edit', False)
		super(RiffForm, self).__init__(*args, **kwargs)

	def clean(self):
		# get cleaned data
		data = super(RiffForm, self).clean()

		# get tab data from cleaned data, convert from unicode string and remove CR
		tab = str(data.get('tab')).replace('\r', '')
		# get audio data
		audio = data.get('audio_file')

		# get default value for tab field and remove newlines from the end
		default_tab = Riff.TAB_DEFAULT.strip('\n')

		# if audio doesn't exist and tab doesn't exist or is the default value
		if not audio and (not tab or tab == default_tab):
			raise ValidationError('Must provide either a tab or an audio file')

	def clean_name(self):
		name = self.cleaned_data.get('name')

		# if this form is editing a riff model, don't check for duplicate name
		if self.edit:
			return name

		if Riff.objects.filter(name=name).exists():
			raise ValidationError('Riff names must be unique')

		return name
	
	AUDIO_EXTENSIONS = ['.wav', '.mp3']

	#Cleans the tags and makes sure no 2 tags have the exact same tags
	def clean_tags(self):
		tags = self.cleaned_data.get('tags')
	
		if self.edit:
			return tags

		if Riff.objects.filter(tags=tags).exists():
			raise ValidationError('Riff tags must be unique')

		return tags
	
	def clean_audio_file(self):
		audio_file = self.cleaned_data.get('audio_file')

		if not audio_file:
			return audio_file

		_, file_extension = splitext(audio_file.name)

		if not file_extension in self.AUDIO_EXTENSIONS:
			raise ValidationError('Invalid file extension: type must be one of ' + ', '.join(self.AUDIO_EXTENSIONS))

		return audio_file
	
	DOCUMENT_EXTENSIONS = ['.pdf', '.odt', '.odg', '.odp'] + Riff.IMAGE_EXTENSIONS

	def clean_document(self):
		document = self.cleaned_data.get('document')

		if not document:
			return  document

		_, file_extension = splitext(document.name)

		if not file_extension in self.DOCUMENT_EXTENSIONS:
			raise ValidationError('Invalid file extension: type must be one of ' + ', '.join(self.DOCUMENT_EXTENSIONS))
		
		return document
