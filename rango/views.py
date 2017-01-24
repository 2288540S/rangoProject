from django.shortcuts import render
from os import linesep
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    message = "Rango says here is the about page.   <a href='/rango/'>Index</a>"
    return HttpResponse(message)
    #return render(request, 'rango/about.html')

