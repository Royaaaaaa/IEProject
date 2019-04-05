from django.shortcuts import render

from django.http import *

from .models import *

import json

def index(request):
    return render(request,'app01/index1.html')

def marinefamily(request):
    typelist= Type.objects.all()
    context={'typelist': typelist}
    return render(request,'app01/marinefamily.html',context)

def marinelife(request,id):
    type = Type.objects.get(pk=id)
    animalList = type.animal_set.all()
    # context={'animalList':animalList}
    context={'animalList':animalList,'typeid':id}
    return render(request,'app01/marinelife.html',context)

def recyclevideo(request):
    return render(request,'app01/recyclevideo.html')
def game(request):
    return render(request,'app01/game.html')
def aboutUs(request):
    return render(request,'app01/aboutUs.html')

def search(request):
    typelist = Type.objects.all()
    context={"typeList":typelist}
    return render(request,'app01/search.html',context)

def searchtype(req):
    type_id = req.GET.get('type')
    type = Type.objects.get(pk=type_id)
    life_list = type.animal_set.all()
    life_dic = {}
    for animal in life_list:
        life_dic[animal.id] = animal.aName
    life_dic = json.dumps(life_dic)
    return HttpResponse(life_dic)

def showDetail(request,id):
    animal = Animal.objects.get(pk=id)
    locationList = animal.location_set.all()
    list = []
    for location in locationList:
        lat = location.latAnimal
        lon = location.lonAnimal
        s=(lat,lon)
        list.append(s)
    context={'animal': animal.id,'locationList':list}
    x = json.dumps(context)
    return render(request,'app01/showDetail.html',locals())

def yellow(request):
    return render(request,'app01/giftest.html')