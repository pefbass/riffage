# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    bio = models.CharField(max_length=2000, default="TEST")
    account_public = models.BooleanField(default=True)

def publish(self):
    self.save()

def __return__username__(self):
    return self.username
    