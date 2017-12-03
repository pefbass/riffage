from os.path import basename, splitext
from django.db import models
from django.forms import forms
from riffage.account.models import Profile
from riffage.collection.custom import SeparatedValuesField

class Riff(models.Model):
	name = models.CharField(max_length=20)

	# This is the check-box for Private Visibility.
	# We default all riffs as Private (checked).
	priv_vis = models.BooleanField(default=True, verbose_name='Private')

	author = models.ForeignKey(
			Profile,
			on_delete=models.CASCADE,
			null=True)

	KEY_CHOICES = [
		('', 'Select'),

		('Amaj', 'Amaj'),
		('Bmaj', 'Bmaj'),
		('Cmaj', 'Cmaj'),
		('Dmaj', 'Dmaj'),
		('Emaj', 'Emaj'),
		('Fmaj', 'Fmaj'),
		('Gmaj', 'Gmaj'),
		('Abmaj', 'Abmaj'),
		('Bbmaj', 'Bbmaj'),
		('Dbmaj', 'Dbmaj'),
		('Ebmaj', 'Ebmaj'),
		('Gbmaj', 'Gbmaj'),

		('Amin', 'Amin'),
		('Bmin', 'Bmin'),
		('Cmin', 'Cmin'),
		('Dmin', 'Dmin'),
		('Emin', 'Emin'),
		('Fmin', 'Fmin'),
		('Gmin', 'Gmin'),
		('Abmin', 'Abmin'),
		('Bbmin', 'Bbmin'),
		('Dbmin', 'Dbmin'),
		('Ebmin', 'Ebmin'),
		('Gbmin', 'Gbmin'),

		('Chromatic', 'Chromatic'),
	]

	riff_key = models.CharField(max_length=20, choices=KEY_CHOICES, default='Select', verbose_name='Key')

	timesig_num = models.IntegerField(default=4, verbose_name='Time Signature Numerator')

	TIMESIG_DENOM_CHOICES = [
		(1, '1'),
		(2, '2'),
		(4, '4'),
		(8, '8'),
		(16, '16'),
		(32, '32'),
	]

	timesig_denom = models.IntegerField(choices=TIMESIG_DENOM_CHOICES, default=4, verbose_name='Time Signature Denominator')

	audio_file = models.FileField(upload_to='riff_audio/', blank=True, null=True, verbose_name='Audio File')
	
	desc = models.TextField(max_length=200, default='', blank=True, verbose_name='Description')

	TAB_DEFAULT = 'G |----|\nD |----|\nA |----|\nE |----|\n'

	tab = models.TextField(max_length=1000, default=TAB_DEFAULT, verbose_name='Tablature')

	tags = models.CharField(max_length=50, default='')

	TAGS_HOLDER = [SeparatedValuesField(tags)]

	document = models.FileField(upload_to='riff_documents/', blank=True, null=True, verbose_name='Documentation')

	def document_filename(self):
		return basename(self.document.name) if self.document else ''

	IMAGE_EXTENSIONS = ['.png', '.jpeg', '.jpg', '.gif', '.svg', '.bmp']

	def document_is_image(self):
		if not self.document:
			return
		
		_, document_extension = splitext(self.document.name)

		return document_extension in self.IMAGE_EXTENSIONS

