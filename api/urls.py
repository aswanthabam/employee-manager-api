from django.urls import path, include
from rest_framework import routers 

urlpatterns = [
    #path('auth/token', ObtainTokenView.as_view()),
    path('auth/',include('api.auth.urls')),
    path('employee/',include('api.employee.urls')),
    path('organization/',include('api.organization.urls'))
]