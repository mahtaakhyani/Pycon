from django.urls import path
from . import views

urlpatterns = [
 
    path('register/', views.RegisterFields.as_view() ),
    path('regdata/', views.RegData.as_view() ),
    path('successreg/', views.SuccessfulRegistration.as_view() ),

 ]
