from django.db import models


class SeparatedValuesField(models.TextField):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
    	if value is None:
    		return value
    	return value.split(self.token)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Riff(models.Model):
	name = models.CharField(max_length=20)

	KEY_CHOICES = [
		('', 'Select'),

		('Amaj', 'Amaj'),
		('Bmaj', 'Bmaj'),
		('Cmaj', 'Cmaj'),
		('Dmaj', 'Dmaj'),
		('Emaj', 'Emaj'),
		('Fmaj', 'Fmaj'),
		('Gmaj', 'Gmaj'),
		('Abmaj', 'Abmaj'),
		('Bbmaj', 'Bbmaj'),
		('Dbmaj', 'Dbmaj'),
		('Ebmaj', 'Ebmaj'),
		('Gbmaj', 'Gbmaj'),

		('Amin', 'Amin'),
		('Bmin', 'Bmin'),
		('Cmin', 'Cmin'),
		('Dmin', 'Dmin'),
		('Emin', 'Emin'),
		('Fmin', 'Fmin'),
		('Gmin', 'Gmin'),
		('Abmin', 'Abmin'),
		('Bbmin', 'Bbmin'),
		('Dbmin', 'Dbmin'),
		('Ebmin', 'Ebmin'),
		('Gbmin', 'Gbmin'),

		('Chromatic', 'Chromatic'),
	]

	riff_key = models.CharField(max_length=20, choices=KEY_CHOICES, default='Select')

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

	audio_file = models.FileField(upload_to='riffs/', blank=True, null=True)
	
	desc = models.TextField(max_length=200, default='')

	tab = models.TextField(max_length=1000, default='G |----|\nD |----|\nA |----|\nE |----|\n')

	tags = models.TextField(max_length=50, default='')
