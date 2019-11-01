from django.shortcuts import render


from django.shortcuts import render

from django.http.response import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from user.serializers import *
import requests


class RegisterFields(APIView):


	def get(self,request):
		return render(
			request,
			''   # main page of registration
			)



	def post(self , request):
		serializer = RequestRegisterSerializer(data=request.data)
		if serializer.is_valid():
			# user.set_unusable_password()
			u = serializer.save()
			set_cookie('user_auth', str(serializer.data['id']) , max_age=None)
			return Response(
				{
					'status' : '200'

				},
				status = status.HTTP_200_OK,
				)
		else:
			return Response(
				serializer.errors,
				{
					'status' : '400'

				},
				status=status.HTTP_400_BAD_REQUEST,
			)

			



class RegData(APIView):

	def get(self,request):
			return render(
				request , '' # user registration data table page

			)





class SuccessfulRegistration(APIView):


	def user_informing(userdata):

		API_Key = '39506F6B44424C352B73314F41656A5244386C656342614D77453539367343494C7A62745A794D793833413D' #kavenegar api key
		url = 'https://api.kavenegar.com/v1/%s/sms/send.json' %API_Key #kavenegar user url
		inform_data = {
			'receptor' : str(userdata['phonenum']) , 
			'message': 'You have registered for pycon 2020 successfuly'
		}

		response = requests.post(url , data = inform_data)
		return response



	def get(self, request):

		activated_user = CustomUser.objects.filter(id = request.COOKIES['user_auth'])
		activated_user['activate'] = True

		if activated_user['activate'] == True:
			user_informing(activated_user)

			return render(
				request ,
				'' # landing page
				,
				{
					'response' : 'registration completed successfuly',
					'status' : 200	

				},
				status = status.HTTP_200_OK
				 )
		else:
			return render(
				request ,
				{
					'error' : 'user has not been activated',
					'status' : '400'
				},
				status=status.HTTP_400_BAD_REQUEST,

				)










