from django.shortcuts import render
from users.models import Document
from share.forms import TextForm

# Create your views here.

def index(request):
    return render(request, "share/index.html", {'document': TextForm()})