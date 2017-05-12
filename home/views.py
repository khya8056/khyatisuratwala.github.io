from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def att(request):
    return render(request,'att.html')

def pot(request):
    return render(request,'pot.html')

def re(request):
    return render(request,'re.html')

def res(request):
    return render(request,'resume.html')