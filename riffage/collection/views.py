from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import NewRiffForm
from .models import Riff

def index(request):
	riffs = Riff.objects.all()
	return render(request, 'collection/index.html',
		{ 'riffs' : riffs })

def new_riff(request):
	if request.method == 'POST':
		form = NewRiffForm(request.POST)

		if form.is_valid():
			riff = Riff()
			riff.name = form.cleaned_data['name']
			riff.save()

	else:
		form = NewRiffForm()
	
	return render(request, 'collection/new_riff.html', {'form': form})
