
#-*- coding: utf-8 -*-
#from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import serializers
#from django.core.serializers import serialize

from ong.models import action
# !! les noms des class models devraient commencer par une Majuscule !!

# Create your views here.

#def home(request):
#    return redirect('http://cartong.github.io/mada-front/dist/atlas/index.html', permanent=True)
def home(request):
    template = loader.get_template('ong/base.html')
    #return HttpResponse(templates/ong/base.html)
    return HttpResponse(template.render())

def get_actions(request):
    actions = action.objects.all()
    data = serializers.serialize('json', actions)
    return HttpResponse(data)
    
def get_actions_by_title(request, title):
    actions = action.objects.filter(titre=title)
    data = serializers.serialize('json', actions)
    return HttpResponse(data)    

def get_geoactions(request):
    actions = action.objects.all()
    data = serializers.serialize('geojson', actions, srid='4326', fields = ( 'titre' , 'description' , 'organisme' , 'categories' , 'duree', 'localisation', 'illustration', 'responsable', 'avancement', 'geom',))
    return HttpResponse(data)

def api_action(request, id):
    if request.method == 'GET':
        action = action.objects.get(pk=id)
        data = serializers.serialize('geojson', action)
        return HttpResponse(data)
    elif request.method == 'POST':
        action = action.objects.get(pk=id)
        action.title = request.post.title
        action.description = request.post.description
        action.save()
        return HttpResponse('OK')    

def faritra(request):
    if request.method == "GET":
    data = open('../static/json/faritra.json')
	faritra = serializers.serialize('json', data)
	return HttpResponse(faritra)
