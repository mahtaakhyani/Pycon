from django.contrib.auth.models import User
from user.models import *
from upload.models import *
from rest_framework import serializers



class RequestRegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUser
		fields = ('id','name_fa' , 'name_en' , 'last_name' , 'codemli' , 'phonenum' , 
		'email' , 'workplace' , 'address' , 'postalcode' , 'activate')





class RequestUploadSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomUserUpload
		fields = ('id' ,'name_fa' , 'name_en' , 'last_name' , 'codemli' , 'phonenum' , 
		'email' , 'workplace' , 'address' , 'postalcode' , 'activate' )
		exclude = ('password')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"








