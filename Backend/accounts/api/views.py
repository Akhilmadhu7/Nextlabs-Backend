from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import Accounts



# for user user login and getting token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)
        
        
        # Add custom claims
        token['username'] = user.username
        token['is_admin'] = user.is_admin
        token['user_points'] = user.user_points
        return token
                
        
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


#for admin and getting token
class AdminTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)
        
        
        # Add custom claims
        token['username'] = user.username
        token['is_admin'] = user.is_admin
        return token
                
        
class AdminTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

 

