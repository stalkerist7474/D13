from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, InvalidCodeView, RegistrationComplite, VerifiedCodeView

urlpatterns = [
     path('login/', 
         LoginView.as_view(template_name = 'sign/login.html'), 
         name='login'),
     path('logout/', 
         LogoutView.as_view(template_name = 'sign/logout.html'), 
         name='logout'),
     path('signup/', 
         BaseRegisterView.as_view(template_name = 'sign/signup.html'), 
         name='signup'),

     path('signup/verified_code_page/',
          VerifiedCodeView.as_view(template_name = 'sign/verified_code_page.html'), name='verified_code'),

     path('signup/invalid_code_page/',
          InvalidCodeView.as_view(template_name = 'sign/invalid_code_page.html'), name='invalid_code'),

     path('signup/registration_complite_page/', 
          RegistrationComplite.as_view(template_name = 'sign/registration_complite.html'), name='registration_complite'),







]