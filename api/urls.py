from django.urls import path, include
from rest_framework import routers 

urlpatterns = [
    #path('auth/token', ObtainTokenView.as_view()),
    path('auth/',include('api.auth.urls')),
    # path('employee/',include('api.employee.urls')),
    path('organization/<int:organization_id>/department/<int:department_id>/employee/',include('api.employee.urls')),
    path('organization/<int:organization_id>/department/',include('api.department.urls')),
    path('organization/',include('api.organization.urls')),
    
]