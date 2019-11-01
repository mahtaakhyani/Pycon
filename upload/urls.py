from django.urls import path
from . import views

urlpatterns = [
 
    path('uploadfile/', views.UploadFields.as_view()),
    path('successupload/', views.UserUploadData.as_view()),

 ]
