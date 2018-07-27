from django.template import Template, Context
from django.http import HttpResponse
import datetime
from django.shortcuts import render

def hello(request):
    return HttpResponse("I love Python! ^-^")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def LovePython(request):
    return render(request, 'lyf/page.html')



def ilovewxy(request):
    return render(request, 'lyf/ilovewxy.html')

