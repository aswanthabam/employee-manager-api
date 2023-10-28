from rest_framework import views, permissions, status
from rest_framework.response import Response
from datetime import datetime
from .serializers import *
from .authentication import JWTAuthentication
from ..models import CustomUser as User
from django.db.models import Q

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(views.APIView):
    def post(self, request):
      try:
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():  
            serializer.save() 
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
      except Exception as e:
          return Response({"status":"internal-error","message":"An unexpected error occured"})
        
 
 
# AUTHORIZATION: Bearer <TOKEN>
class ObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.filter(username=username).first()
        # print(user.check_password(password),password,user.password)
        if user is None or not user.password== password:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the JWT token
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({'token': jwt_token})