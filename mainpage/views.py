from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    context = {'name' : 'home'}
    return render(request, 'mainpage/home.html', context)

def contact(request):
    context = {'name' : 'contact'}
    return render(request, 'mainpage/contact.html', context)

def aboutus(request):
    context = {'name' : 'aboutus'}
    return render(request,'mainpage/aboutus.html', context)