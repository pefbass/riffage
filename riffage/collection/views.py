from django.http import *
from django.shortcuts import render, get_object_or_404
from .forms import RiffForm
from .models import Riff

def index(request):
	riffs = Riff.objects.all()
	return render(request, 'collection/index.html',
		{ 'riffs' : riffs })

def new_riff(request):
	if request.method == 'POST':
		form = RiffForm(request.POST, request.FILES)

		if form.is_valid():
			riff = Riff()
			data = form.cleaned_data

			for key in data:
				setattr(riff, key, data[key])

			riff.save()

			return render(request, 'collection/riff_detail.html', {'riff': riff})

	else:
		form = RiffForm()

	return render(request, 'collection/new_riff.html', {'form': form})

def riff_detail(request, pk):
	riff = get_object_or_404(Riff, pk=pk)
	return render(request, 'collection/riff_detail.html', {'riff': riff})

def riff_edit(request, pk):
    riff = get_object_or_404(Riff, pk=pk)
    if request.method == "POST":
        form = RiffForm(request.POST, instance=riff)
        if form.is_valid():
            riff = form.save(commit=False)
            riff.save()
            return redirect('riff_detail', pk=riff.pk)
    else:
        form = RiffForm(instance=riff)
    return render(request, 'collection/riff_edit.html', {'form': form})
