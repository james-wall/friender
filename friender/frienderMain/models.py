import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class User(models.Model):
	id = models.AutoField() # internal unique identifier
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=200)
	username = models.CharField(max_length-30) # how people will exchange social media information
	facebookProfileURL = models.TextField(validators=[URLValidator()])
	twitterProfileURL = models.TextField(validators=[URLValidator()])
	creationDate  = models.DateTimeField('date published') #todo remove this and run makemigrations, then migrate

	def __str__(self):
		return self.firstName

	def was_published_recently(self):
		return self.creationDate >= timezone.now() - datetime.timedelta(days=1)

	def validateURL(url)
		validate = URLValidator(verify_exists=True)
		try:
			validate(url)
		except ValidationError, e:
			print e

   # TODO add urls for social media