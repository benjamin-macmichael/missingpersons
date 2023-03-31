#You need to import the render function in order to call it
from django.shortcuts import render
#This is the name of the view function that will be called by the “” url
def indexPageView(request) :
    return render(request, 'persons/index.html')

def aboutPageView(request) :
    return render(request, 'persons/about.html') 

def actPageView(request):
    return render(request, 'persons/act.html') 

def contactPageView(request):
    return render(request, 'persons/contact.html')