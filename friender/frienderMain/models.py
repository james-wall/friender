import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

class User(models.Model):
	#id = models.AutoField() # internal unique identifier
	firstName = models.CharField(max_length=30, default='test')
	lastName = models.CharField(max_length=200, default='test')
	username = models.CharField(max_length=30, default='test') # how people will exchange social media information
	emailAddress = models.CharField(max_length=30, default='fakenewsemail@fakenews.com')
	facebookProfileURL = models.TextField(validators=[URLValidator()], default = 'https://www.facebook.com/')
	twitterProfileURL = models.TextField(validators=[URLValidator()], default = 'https://www.twitter.com/')
	creationDate  = models.DateTimeField('date published') #todo remove this and run makemigrations, then migrate

	def __str__(self):
		return self.firstName

	def was_published_recently(self):
		return self.creationDate >= timezone.now() - datetime.timedelta(days=1)

	def validateURL(url):
		validate = URLValidator(verify_exists=True)
		try:
			validate(url)
		except ValidationError as e:
			print(e)


# TODO add urls for social media