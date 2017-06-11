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
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
def d1(request):
	return render(request, 'd1/d1.html')
