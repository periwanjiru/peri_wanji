from django.shortcuts import render
from django.http import HttpResponse
#from .models import Blog

# Create your views here.



def Welcome(request):
    return HttpResponse("<p>Welcome to Akirachix class <p>")
def Students(request):
    return HttpResponse("<p>Welcom to our class 2017, feel at school<p>")
def Teachers(request):
     return HttpResponse("<p>Welcom to our class 2017,Here are ourstudents <p>")
        
       
    

# def lists(request):
#   return(request, 'index.html')
# def create(request):
#      return HttpResponse("hello world")
# def details(request):
#     pass
# def update(request):
#     pass
# def delete(request):
#     pass
