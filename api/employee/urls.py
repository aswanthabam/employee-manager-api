from django.urls import path, include
from .views import *
from rest_framework import routers 

urlpatterns = [
    path('',EmployeeView.as_view()),
    path('create/',EmployeeView.as_view()),
    path('update/',EmployeeView.as_view()),
    path('delete/',EmployeeView.as_view())
]