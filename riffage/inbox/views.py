from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth

def inbox(request):
	params = {}
	params['category'] = 'inbox'
	return render(request, 'inbox.html',
		{'params': params,})