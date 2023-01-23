from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q
from rest_framework import status
from . models import Accounts,ApplicationModel,TaskModel
from . serializers import AccountSerializer, ApplicationSerializer, TaskSerializer,TaskCompletedSerialzier
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import ListAPIView


# Create your views here.


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
            data['Error'] = serializer.errors
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


#user profile fucntion.
class UserProfile(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        data = {}
        user = request.user.id #getting user from the request data
        print('here is user',user)
        try:
            accounts = Accounts.objects.get(id=user)
        except:
            data['Response'] = 'Account does not exist'
            return Response(data, status=status.HTTP_404_NOT_FOUND)   
        if accounts:
            serializer = AccountSerializer(accounts)
            data['Response'] = serializer.data
            return Response(data,status=status.HTTP_200_OK) 


class TaskComplete(APIView):

    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser,FormParser)

    def post(self,request):
        data = {}
        print('here is data',request.data)
        try:
            task = TaskModel.objects.get(Q(application=self.request.data['application']) & Q(user=self.request.data['user']))
            print('taskkkkk',task)
        except:
            print('helksad')
            task = None

        if task is None:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                print('serialiae')
                serializer.save()
                user = Accounts.objects.get(id=request.user.id)
                user.user_points = int(user.user_points) + 100
                user.save()
                print('userpoints',user.user_points)
                data['Response'] = 'Application downloaded'
                return Response(data,status=status.HTTP_201_CREATED)
            else:
                data['Response'] = serializer.errors
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        else:   
            data['Response'] = 'Task already completed'
            return Response(data, status=status.HTTP_208_ALREADY_REPORTED)      
             

    def get(self,request):
        user = request.user.id
        tsk = TaskModel.objects.filter(user = user)
        data = {}
        ser = TaskCompletedSerialzier(tsk,many=True,context={'request':request})
        data['Res'] = ser.data
        return Response(data,status=status.HTTP_200_OK)
        
#to show the detail of an app.
class AppDetailsView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,id):
        data = {}
        try:
            app = ApplicationModel.objects.get(id=id)
        except:
            data['Response'] = 'Something went wrong'
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        if app:
            serializer = ApplicationSerializer(app,context={'request':request})
            data['Response'] = serializer.data
            return Response(data,status=status.HTTP_200_OK)

                
