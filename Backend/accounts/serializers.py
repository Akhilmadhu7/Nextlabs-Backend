import json
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import serializers
from . models import Accounts, ApplicationModel,TaskModel
from django.db.models import Q
import re


#Account serialzer
class AccountSerializer(serializers.ModelSerializer):

    #for confirmation password
    password2 = serializers.CharField(
        style={'input': 'password'}, write_only=True)

    class Meta:
        model = Accounts
        fields = ['username','email','password','password2','user_points']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        #validating the input data are valid or not.
        email = attrs['email']
        email_pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]{2,5}\.[a-z]{2,3}$"
        email_verify = re.match(email_pattern, email)

        if email_verify is None:
            raise serializers.ValidationError(
                {"email": "Enter valid email"})

        password = attrs['password']
        password2 = attrs['password2']
        password_pattern = re.compile(r'^[a-zA-Z0-9]{8}[0-9]*[A-Za-z]*$')
        password_verify = password_pattern.search(password)
        password2_verify = password_pattern.search(password2)

        if password_verify is None:
            raise serializers.ValidationError({
                "Password":"Password should contain minimum 8 characters including numbers"
            })
        if password2_verify is None:
            raise serializers.ValidationError({
                "password2":"Confirm Password should contain minimum 8 characters including numbers"
            })    
        if password != password2:
            raise serializers.ValidationError({
                "Password2":"Password must match"
            })   
        return   attrs

    def save(self):
        register = Accounts(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )    
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        register.set_password(password)
        register.save()    
        return register


class ApplicationSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ApplicationModel
        fields = '__all__'
       

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TaskModel
        fields = '__all__'

    # def validate(self, attrs):
    #     self.application = attrs['application']
    #     print('adlk',self.application)
    #     self.user = attrs['user']
    #     task = TaskModel.objects.get(Q(application=self.application) & Q(user=self.user))     
    #     if task is not None:
    #         raise serializers.ValidationError({'Task':"Task completed already"})


class TaskCompletedSerialzier(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        fields = '__all__'
        depth = 1

    

      
        
    
    