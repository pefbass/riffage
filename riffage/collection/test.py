from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile

from .forms import RiffForm
from .models import Riff

class NewRiffTest(TestCase):

	def test_valid_data(self):
		form = RiffForm({
			'name': 'My New Riff',
			'priv_vis': False,
			'riff_key': 'Amaj',
			'timesig_num': 4,
			'timesig_denom': 4,
			'desc': 'A really great riff!',
			'tab': 'G |----|\nD |----|\nA |----|\nE |0000|\n',
			'tags': 'sweaty, slimy'
		},
		{
			'audio_file': SimpleUploadedFile('song.mp3', bytes(1234)),
			'document': SimpleUploadedFile('song.pdf', bytes(1234))
		})

		self.assertTrue(form.is_valid())

		riff = form.save()
		self.assertEqual(riff.name, 'My New Riff')
		self.assertEqual(riff.priv_vis, False)
		self.assertEqual(riff.riff_key, 'Amaj')
		self.assertEqual(riff.timesig_num, 4)
		self.assertEqual(riff.timesig_denom, 4)
		self.assertEqual(riff.desc, 'A really great riff!')
		self.assertEqual(riff.tab, 'G |----|\nD |----|\nA |----|\nE |0000|')
		self.assertEqual(riff.tags, 'sweaty, slimy')

	def test_duplicate_name(self):
		form = RiffForm({
			'name': 'My Riff',
			'priv_vis': False,
			'riff_key': 'Amaj',
			'timesig_num': 4,
			'timesig_denom': 4,
			'desc': 'A really great riff!',
			'tab': 'G |----|\nD |----|\nA |----|\nE |0000|\n',
			'tags': 'sweaty, slimy'
		})

		form.save()

		form_duplicate_name = RiffForm({'name': 'My Riff'})
		self.assertIn('name', form_duplicate_name.errors)
		self.assertEqual(form_duplicate_name.errors['name'], ['Riff names must be unique'])
	
	def test_invalid_audio_filetype(self):
		form = RiffForm({}, {'audio_file': SimpleUploadedFile('song.jpg', bytes(1234))})

		error_message = 'Invalid file extension: type must be one of ' + ', '.join(RiffForm.AUDIO_EXTENSIONS)

		self.assertIn('audio_file', form.errors)
		self.assertEqual(form.errors['audio_file'], [error_message])

	def test_no_tab_or_audio(self):
		form = RiffForm({
			'name': 'My Riff',
			'priv_vis': False,
			'riff_key': 'Amaj',
			'timesig_num': 4,
			'timesig_denom': 4,
			'desc': 'A really great riff!',
			'tab': Riff.TAB_DEFAULT,
			'tags': 'sweaty, slimy'
		})

		self.assertEqual(form.non_field_errors(), ['Must provide either a tab or an audio file'])

	def test_invalid_document_filetype(self):
		form = RiffForm({}, {'document': SimpleUploadedFile('song.docx', bytes(1234))})

		error_message = 'Invalid file extension: type must be one of ' + ', '.join(RiffForm.DOCUMENT_EXTENSIONS)

		self.assertIn('document', form.errors)
		self.assertEqual(form.errors['document'], [error_message])
