from rest_framework import views, permissions, status
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from ..authentication import JWTAuthentication
from ..models import CustomUser as User
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class EmployeeView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,organization_id,department_id):
        try:
            org = Organization.objects.filter(organization_id=organization_id,user=request.user).first()
            if org == None:
               return Response({"status": "success", "message":"Invalid organization"}, status=status.HTTP_400_OK) 
            dept = Department.objects.filter(department_id=department_id,organization=org).first()
            if dept == None:
               return Response({"status": "success", "message":"Invalid department"}, status=status.HTTP_400_OK)
            empls = Employee.objects.filter(department=dept)
            serializer = EmployeeSerializer(empls,many=True,context={'user':request.user})
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
        except Exception as e:
            return Response({"status":"internal-error","message":"An unexpected error occured"})
    def post(self, request,organization_id,department_id):
      try:
        org = Organization.objects.filter(organization_id=organization_id,user=request.user).first()
        if org == None:
            return Response({"status": "success", "message":"Invalid organization"}, status=status.HTTP_400_OK) 
        dept = Department.objects.filter(department_id=department_id,organization=org).first()
        if dept == None:
            return Response({"status": "success", "message":"Invalid department"}, status=status.HTTP_400_OK)
        serializer = EmployeeSerializer(data=request.data,context={'department':dept})
        if serializer.is_valid():  
            serializer.save() 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
          return Response({"status":"internal-error","message":"An unexpected error occured"})

    def put(self, request,organization_id,department_id):
      try:
        org = Organization.objects.filter(organization_id=organization_id,user=request.user).first()
        if org == None:
            return Response({"status": "success", "message":"Invalid organization"}, status=status.HTTP_400_OK)
        dept = Department.objects.filter(department_id=department_id,organization=org).first()
        if dept == None:
            return Response({"status": "success", "message":"Invalid department"}, status=status.HTTP_400_OK)
        instance = Employee.objects.filter(employee_id = request.data.get('employee_id'),department=dept).first()
        if instance == None:
           return Response({'status':'error','message':'invalid employee id'})
        
        serializer = EmployeeUpdateSerializer(instance,data=request.data)
        if serializer.is_valid():  
            serializer.save() 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
          return Response({"status":"internal-error","message":"An unexpected error occured"})


    def delete(self, request,organization_id,department_id):
      try:
        org = Organization.objects.filter(organization_id=organization_id,user=request.user).first()
        if org == None:
            return Response({"status": "success", "message":"Invalid organization"}, status=status.HTTP_400_OK)
        dept = Department.objects.filter(department_id=department_id,organization=org).first()
        if dept == None:
            return Response({"status": "success", "message":"Invalid department"}, status=status.HTTP_400_OK)
        instance = Employee.objects.filter(employee_id = request.data.get('employee_id'),department=dept).first()
        if instance == None:
           return Response({'status':'error','message':'invalid employee id'})
        instance.delete()
        return Response({"status": "success", "message":"successfully deleted employee"}, status=status.HTTP_200_OK) 
      except Exception as e:
          return Response({"status":"internal-error","message":"An unexpected error occured"})
    