from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'mainpage/home.html')

def contact(request):
    return render(request, 'mainpage/contact.html')

def aboutus(request):
    return render(request, 'mainpage/aboutus.html')

def activities(request):
    return render(request, 'mainpage/activities.html')

def specific(request):
    return render(request, 'mainpage/activity-specific.html')    

def login(request):
    if request.method == 'POST':
        ##do some validation stuff
        pass
    else: 
        #should raise error 
        pass

def sign(request):
    if request.method == 'POST':            
        #register the user
        pass 
    else: 
        #should raise error  
        pass  