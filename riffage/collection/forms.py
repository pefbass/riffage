from django import forms

class NewRiffForm(forms.Form):
	name = forms.CharField(label='Riff Name', max_length='100')
