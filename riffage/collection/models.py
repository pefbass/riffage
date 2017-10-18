from django.db import models

class Riff(models.Model):
	name = models.CharField(max_length=100)

	KEY_CHOICES = [
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D'),
		('E', 'E'),
		('F', 'F'),
		('G', 'G'),
		('Ab', 'Ab'),
		('Bb', 'Bb'),
		('Db', 'Db'),
		('Eb', 'Eb'),
		('Gb', 'Gb'),
	]

	riff_key = models.CharField(max_length=2, choices=KEY_CHOICES, default='A')

	timesig_num = models.IntegerField(default=4)

	TIMESIG_DENOM_CHOICES = [
		(1, '1'),
		(2, '2'),
		(4, '4'),
		(8, '8'),
		(16, '16'),
		(32, '32'),
	]

	timesig_denom = models.IntegerField(choices=TIMESIG_DENOM_CHOICES, default=4)
