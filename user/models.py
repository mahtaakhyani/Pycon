from django.db import models
from django.contrib.auth.models import User , AbstractBaseUser 
from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

from langdetect import detect


class CustomUser(AbstractUser):

	name_fa = models.CharField(
		max_length=100 , unique=True)
	name_en = models.CharField(
		max_length=100 , unique=True)
	workplace = models.CharField(
		max_length=100 , unique=True)
	codemli = models.IntegerField(
		max_length=11)
	phonenum = models.IntegerField(
		max_length=12)
	postalcode = models.IntegerField(
		max_length=11 , default = 0)
	address = models.CharField(
		max_length=200 , default = None)
	activate = models.BooleanField(default = False)

	def valid(self):
		if len(self.codemli) != 10 or type(self.codemli) != int :
			raise ValidationError("Not Valid")

		elif len(self.phonenum) != 10 or type(self.phonenum) != int :
			raise ValidationError("Not Valid")

		elif len(self.postalcode) not in range(0,11) or type(self.phonenum) != int :
			raise ValidationError("Not Valid")


		elif 'sw' not in detect(self.name_en)  or 'ur' not in detect(self.name_fa):
			raise ValidationError("Not Valid")






