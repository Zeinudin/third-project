from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.conf import settings

class Diary(models.Model):
	time_now = models.DateTimeField(default=timezone.now)
	text = models.CharField(max_length=50)
	do_exercises = models.BooleanField(default=True)
	SCALE_NUMBER = [(str(i), str(i)) for i in range(1,11)]
	scale = models.CharField(
		max_length=2,
		choices=SCALE_NUMBER, 
		default=SCALE_NUMBER[0])

	def __str__(self):
		return str(self.time_now)