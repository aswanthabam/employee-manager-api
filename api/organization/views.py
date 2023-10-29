from rest_framework import views, permissions, status
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from ..authentication import JWTAuthentication
from ..models import CustomUser as User
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class OrganizationView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            org_id =request.GET.get('organization_id')
            if org_id:
              orgs = Organization.objects.filter(user=request.user,organization_id=org_id)
            else:
               orgs = Organization.objects.filter(user=request.user)
            serializer = OrganizationSerializer(orgs,many=True,context={'user':request.user}) 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK) 
        except Exception as e:
            print(e)
            return Response({"status":"internal-error","message":"An unexpected error occured"})
    def post(self, request):
      try:
        serializer = OrganizationSerializer(data=request.data,context={'user':request.user}) 
        if serializer.is_valid():  
            serializer.save() 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
          return Response({"status":"internal-error","message":"An unexpected error occured"})

    def put(self, request):
      try:
        instance = Organization.objects.filter(organization_id = request.data.get('organization_id')).first()
        if instance == None:
           return Response({'status':'error','message':'invalid org id'})
        elif instance.user.username != request.user.username:
           return Response({'status':'error','message':'not allowed to edit this user'})
        
        serializer = OrganizationUpdateSerializer(instance,data=request.data) 
        if serializer.is_valid():  
            serializer.save() 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
          return Response({"status":"internal-error","message":"An unexpected error occured"})


    def delete(self, request):
      try:
        instance = Organization.objects.filter(organization_id = request.data.get('organization_id')).first()
        if instance == None:
           return Response({'status':'error','message':'invalid org id'})
        elif instance.user.username != request.user.username:
           return Response({'status':'error','message':'not allowed to edit this user'})
        instance.delete()
        return Response({"status": "success", "message":"successfully deleted organization"}, status=status.HTTP_200_OK) 
      except Exception as e:
          return Response({"status":"internal-error","message":"An unexpected error occured"})
    
    
        
 