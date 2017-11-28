from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MessageForm
from .models import Message
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

def inbox(request):
	messages = Message.objects.all()
	users = User.objects.all()
	params = {}
	params['category'] = 'inbox'
	return render(request, 'inbox.html',
		{'params': params,
		 'messages': messages})

@csrf_exempt
def send_message(request):
	params = {}
	params['category'] = 'inbox'
	if request.method == 'POST':
		form = MessageForm(request.POST, request.FILES)

		if form.is_valid():
			message = form.save(commit=False)
			message.save()

			return redirect('inbox')

	else:
		form = MessageForm()

	return render(request, 'send_message.html', {'form': form, 'params': params})