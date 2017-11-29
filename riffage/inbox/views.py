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
	user = request.user.username
	return render(request, 'inbox.html',
		{'params': params,
		 'messages': messages,
		 'user': user
		 })


@csrf_exempt
def send_message(request):
	params = {}
	params['category'] = 'inbox'

	if request.method == 'POST':
		send_to_user = request.POST.get('send_to_user')
		subject = request.POST.get('subject')
		message = request.POST.get('message')
		if send_to_user and subject and message:
			msg = Message(message_sent_by=request.user.username, 
						  message_received_by=send_to_user,
						  subject=subject,
						  body=message)
			msg.save()
			params['message_saved'] = True
		else: 
			params['message_saves'] = False
		return JsonResponse(params)

	'''
	if request.method == 'POST':
		form = MessageForm(request.POST, request.FILES)

		if form.is_valid():
			message = form.save(commit=False)
			message.save()

			return redirect('inbox')

	else:
		form = MessageForm()
	'''

	return render(request, 'send_message.html', {'params': params})
	#return render(request, 'send_message.html', {'form': form, 'params': params})