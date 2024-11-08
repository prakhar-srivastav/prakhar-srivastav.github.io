# blog/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def cv(request):
    return render(request, 'cv.html')

def physics(request):
    return render(request, 'physics.html')

def algorithms(request):
    return render(request, 'algorithms.html')

def technology(request):
    return render(request, 'technology.html')

def connect(request):
    return render(request, 'connect.html')
