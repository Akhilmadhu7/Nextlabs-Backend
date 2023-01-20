from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from . models import Accounts,ApplicationModel
from . serializers import AccountSerializer, ApplicationSerializer
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView


# Create your views here.

class Hello(APIView):

    def get(self,request):
        data = {}
        data['a'] = 'hello'

        return Response(data,status=status.HTTP_200_OK)


#Signup function
class SignupView(APIView):

    def post(self,request):
        data = {}
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            accounts = serializer.save()
            data['Response'] = f'Account created succesfully {accounts.username}'
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            data['Error'] = 'Invalid data'
            data['Response'] = serializer.errors
            return Response(data,status=status.HTTP_400_BAD_REQUEST)   


# # #Add application
class AddApplication(APIView):

    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser)
    
    def post(self,request):
        data = {}
        print('requst.data',request.data)
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['Response'] = serializer.data
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            print('error is ',serializer.errors)
            data['Response'] = serializer.errors
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
          

#List all the application on admin side.
class ListApplication(ListAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return ApplicationModel.objects.all()

#delete application
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_app(request,id):
    data = {}
    app = ApplicationModel.objects.get(id=id)
    app.delete()
    data['Response'] = 'Application deleted Succesfully'
    return Response(data,status=status.HTTP_200_OK) 