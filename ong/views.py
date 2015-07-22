#from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

def home(request):
    template = loader.get_template('ong/base.html')
    #return HttpResponse(templates/ong/base.html)
    return HttpResponse(template.render())

#def home(request):
#    return redirect('http://cartong.github.io/mada-front/dist/atlas/index.html', permanent=True)
