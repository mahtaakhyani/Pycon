from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser

from django.conf import settings
from django.core.files.storage import FileSystemStorage


from user.serializers import *

class UploadFields(APIView):
	parser_class = (FileUploadParser,)

	def get(self,request):
		return render(
			request,
			''   # main page of upload
			)


	def post(self , request):
		serializer = RequestUploadSerializer(data=request.data)
		if serializer.is_valid():
			user.set_unusable_password()
			u = serializer.save()
			return Response(
				{
					'status' : '200'

				},
				status = status.HTTP_200_OK
				)

		else:
			return Response(
				serializer.errors,
				{
					'status' : '400'

				},
				status=status.HTTP_400_BAD_REQUEST
			)

	def put(self , request):
		file_serializer = FileSerializer(data = reaquest.data['my_upload_file'])
		if serializer.is_valid():
			file_serializer.save()
			return Response(
				file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(
          	file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


			

class UserUploadData(APIView):

	def get(self,request):
			return render(
				request , '' # user registration data table

			)












