from django.db import models
from django.contrib.auth.models import User , AbstractBaseUser
from rest_framework import serializers

class CustomUserUpload(AbstractBaseUser):

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
		max_length=11)
	address = models.CharField(
        max_length=200 )


class File(models.Model):
    file = models.FileField(blank=False, null=False)