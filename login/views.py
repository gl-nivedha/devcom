from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("home")
def user(request):
    return HttpResponse("user page")    
    



