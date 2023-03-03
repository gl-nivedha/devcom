from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")
def user(request):
    return render(request,"userpage.html")    
    



