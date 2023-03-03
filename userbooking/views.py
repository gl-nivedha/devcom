from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from userbooking.models import booking



# Create your views here.
def book(request):
    if request.method=="POST":
        Contact=request.POST['Contact']
        Reason=request.POST['Reason']
        Council=request.POST['Council']
        Room=request.POST['Room']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        obj = booking(Contact=Contact,Reason=Reason,Council=Council,Room=Room,start_date=start_date,end_date=end_date)
        obj.save()
        print("the data has been saved")
        messages.info(request,"booking successful")
        return redirect('/')
        
        

    else: 
        return render(request,"booking.html")   
        

        


   
