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

	def test_invalid_form_create_page(self):
		form = SignUpForm({
			'username' : 'test_name',
			'email' : 'test_email@gmail.com',
			'password1' : 'password_1',
			'password2' : 'password_2'
		})
		
		self.assertFalse(form.is_valid())

	def test_valid_form_login_page(self):
		self.user = User.objects.create_user(username='testuser', password='password_1')
		login = self.client.login(username='testuser', password='password_1')

		self.assertTrue(login)

	def test_invalid_form_login_page(self):
		self.user = User.objects.create_user(username='testuser', password='password_1')
		login = self.client.login(username='testuser', password='password_2')

		self.assertFalse(login)
	
	def test_user_bio_input(self):
		bio_updated = False
		self.user = User.objects.create_user(username='testuser', password='password_1')
		login = self.client.login(username='testuser', password='password_1')

		if (self.user.profile.bio == ""):
			bio_updated = True

		self.assertTrue(bio_updated)

	def test_user_email(self):
		email_found = False
		self.user = User.objects.create_user(username='testuser', password='password_1')
		login = self.client.login(username='testuser', password='password_1')

		if (self.user.email == ""):
			email_found = True

		self.assertTrue(email_found)

	def test_user_username(self):
		username_found = False
		self.user = User.objects.create_user(username='testuser', password='password_1')
		login = self.client.login(username='testuser', password='password_1')

		if (self.user.username == "testuser"):
			username_found = True

		self.assertTrue(username_found)

	def test_user_privacy(self):
		privacy_accurate = False
		self.user = User.objects.create_user(username='testuser', password='password_1')
		login = self.client.login(username='testuser', password='password_1')

		if (self.user.profile.private_account == True):
			privacy_accurate = True

		self.assertTrue(privacy_accurate)
