from django.db import models

class Spots(models.Model):
	latitude = models.IntegerField(blank=False, default='')
	longitude = models.IntegerField(blank=False, default='')
	occupied = models.BooleanField(default=False)

class Parked(models.Model):
	spot_id = models.IntegerField(blank=False)
	time_slots = models.CharField(max_length=100, blank=True)
