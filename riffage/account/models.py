# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=100)

def publish(self):
    self.save()

def __return__username__(self):
    return self.username
    