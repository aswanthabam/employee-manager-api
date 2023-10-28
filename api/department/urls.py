from django.urls import path, include
from .views import *
from rest_framework import routers 

urlpatterns = [
    path('',DepartmentView.as_view()),
    path('create/',DepartmentView.as_view()),
    path('update/',DepartmentView.as_view()),
    path('delete/',DepartmentView.as_view())
]