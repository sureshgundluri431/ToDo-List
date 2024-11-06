from django.shortcuts import render
from to_do.models import *
from to_do.forms import *
# Create your views here.

def Home(request):
    return render(request,'home.html')

def Task(request):
    return render(request,'Task.html')
