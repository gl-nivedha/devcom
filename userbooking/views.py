from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from userbooking.models import booking
from .serializers import booking_ser
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET','POST'])

    

    
def book(request):
    if request.method=="POST":
        
        serializer=booking_ser(data=request.data)
        try:
            serializer.is_valid(raise_exception="True")
        except :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    else: 
        
        books = booking.objects.all()  
        serializer = booking_ser(books,many=True)  
        return JsonResponse(serializer.data,safe=False)   
    
        

    
        
           
       
       

        
        
    
       


        

        


   
