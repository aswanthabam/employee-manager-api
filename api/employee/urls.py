from django.urls import path, include
from .views import *
from rest_framework import routers 

urlpatterns = [
    #path('auth/token', ObtainTokenView.as_view()),
    path('register/',UserRegistrationView.as_view()),
    path('token/',ObtainTokenView.as_view()),
]