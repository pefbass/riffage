from django.db import models

class Riff(models.Model):
	name = models.CharField(max_length=100)
