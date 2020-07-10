from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
from .models import Portfolio

from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def ArchPort(request):
    project=Portfolio.objects.all()
    return render(request,'pages/architecture.html',{"project":project})
    
def SoftwarePort(request):
    return render(request,'pages/software.html')