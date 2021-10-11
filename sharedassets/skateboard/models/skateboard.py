from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
import pytz

# this is the database schema written in Python
class SkateBoard(models.Model):
	
	# brand value has to be one of these 3 values
	BRAND_CHOICES = (
        ('Baker', 'Baker'),
        ('Birdhouse', 'Birdhouse'),
        ('Krooked', 'Krooked'),
    )
	
	name_owner = models.CharField(max_length=200)
	brand = models.CharField(max_length=50,choices=BRAND_CHOICES)
	weight = models.FloatField(validators=[MinValueValidator(2.0,message="value less than the minimum value"), MaxValueValidator(20.0,message="value more than the maximum value")])
	length = models.FloatField(validators=[MinValueValidator(70.0,message="value less than the minimum value"), MaxValueValidator(90.0,message="value more than the maximum value")])
	location = models.CharField(max_length=200)
	timestamp = models.DateTimeField()
	
	# the availability/status is based on the timestamp and the time at which the request is made. calculated each time 
	# the database record is retrieved
	@property
	def status(self):
		"Returns if the skateboard is available at the time of request"
		if datetime.datetime.now(pytz.utc) >= self.timestamp:
			return "Available"
		else:
			return "Not Available"
				