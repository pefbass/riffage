
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from .forms import SignUpForm

def account(request):
    if request.user.is_authenticated():
        return render(request, 'account.html')
    else:
        return redirect('/')

def create(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/collection', {'user': user})
    else:
        form = SignUpForm()
    return render(request, 'create.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')

def collections(request):
    return redirect('/collection')
