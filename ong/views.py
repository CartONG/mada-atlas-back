#from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.core import serializers

from ong.models import action

# Create your views here.

def home(request):
    template = loader.get_template('ong/base.html')
    #return HttpResponse(templates/ong/base.html)
    return HttpResponse(template.render())

def get_actions(request):
    actions = action.objects.all()
    data = serializers.serialize('json', actions)
    return JsonResponse(data, safe=False)
    
def get_actions_by_title(request, title):
    actions = action.objects.filter(titre=title)
    data = serializers.serialize('json', actions)
    return JsonResponse(data, safe=False)    

#def home(request):
#    return redirect('http://cartong.github.io/mada-front/dist/atlas/index.html', permanent=True)
