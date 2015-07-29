from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, 'mainpage/home.html')

def contact(request):
    return render(request, 'mainpage/contact.html')

def aboutus(request):
    return render(request, 'mainpage/aboutus.html')

def activities(request):
    return render(request, 'mainpage/activities.html')