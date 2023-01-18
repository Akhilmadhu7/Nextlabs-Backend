from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import Accounts
# from accounts.serializers import UserProfileSerializer




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)
        
        
        # Add custom claims
        token['username'] = user.username
        token['is_admin'] = user.is_admin
        return token
                
        
        

    
         
        

        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# class LogoutUserView(APIView):

#     def post(self,request):
#         data = request.data
#         print(type(data))
#         print('hello')
#         user = request.data['username']
#         # accounts = Accounts.objects.get(username=user)
#         return Response({'Response':"ok"})
#         # else:
#         #     return Response({'m':"went wrong"})    
       

          


@api_view(['Get'])
def get_routes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]

    return Response(routes)