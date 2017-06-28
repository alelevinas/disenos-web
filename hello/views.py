import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
#~ def index(request):
    #~ r = requests.get('http://httpbin.org/status/418')
    #~ print(r.text)
    #~ return HttpResponse('<pre>' + r.text + '</pre>')
    
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index2.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
def d1(request):
	return render(request, 'd1/d1Template.html')

def d2(request):
	return render(request, 'd2.html')

def d3(request):
	return render(request, 'd3.html')

def d4(request):
	return render(request, 'd4.html')

def d5(request):
	return render(request, 'd5.html')
	
def d6(request):
	return render(request, 'd6.html')

def d7(request):
	return render(request, 'd7.html')

def zman(request):
    return render(request, 'zman.html')
