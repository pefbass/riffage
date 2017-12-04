# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .forms import SignUpForm
from riffage.account.models import Profile, PasswordResetForm
from django.contrib.auth.models import User

# Create your tests here.

class TestAccountApp(TestCase):
    
    def test_valid_form_create_page(self):
        form = SignUpForm({
			'username' : 'test_name',
            'email' : 'test_email@gmail.com',
            'password1' : 'password_1',
            'password2' : 'password_1'
		})
	self.assertTrue(form.is_valid())

    def test_valid_form_login_page(self):
        self.user = User.objects.create_user(username='testuser', password='password_1')
        login = self.client.login(username='testuser', password='password_1')
	self.assertTrue(login)
