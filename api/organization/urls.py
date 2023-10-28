from django.urls import path, include
from .views import *
from rest_framework import routers 

urlpatterns = [
    path('',OrganizationView.as_view()),
    path('create/',OrganizationView.as_view()),
    path('update/',OrganizationView.as_view()),
    path('delete/',OrganizationView.as_view())
]