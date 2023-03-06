from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from useraccounts.models import register
from .serializers import register_ser, login_ser
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])
def user_register(request):
    if request.method=="POST":
        serializer=register_ser(data=request.data)
        try:
            serializer.is_valid(raise_exception="True")
        except :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        


    else:

        reg = register.objects.all()
        serializer = register_ser(reg,many=True)  
        return JsonResponse(serializer.data,safe=False)   
    
@api_view(['GET','POST'])
def login(request):
    if request.method=="POST":
         serializer=login_ser(data=request.data)
         try:
            serializer.is_valid(raise_exception="True")
         except :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
         else:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        logs = register.objects.all()  
        serializer = login_ser(logs,many=True)  
        return JsonResponse(serializer.data,safe=False)   
    
        

    

    




