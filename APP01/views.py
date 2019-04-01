from django.shortcuts import render

from django.http import *

from .models import *

import json

def index(request):
    return render(request,'app01/index.html')
def marinelife(request):
    # animalList = Animal.objects.all()
    imageList = Image.objects.all()
    # context={'animalList':animalList}
    context={'imageList':imageList}
    return render(request,'app01/marinelife.html',context)
def recyclevideo(request):
    return render(request,'app01/recyclevideo.html')
def game(request):
    return render(request,'app01/game.html')
def aboutUs(request):
    return render(request,'app01/aboutUs.html')

# def search(request):
#     if request.method == "GET":
#         typelist = Type.objects.all()
#     # for type in typelist:
#     #     animalList = type.animal_set.all()
#     #     animaldir[type.id]=animalList
#         context={"typeList":typelist}
#         return render(request,'app01/search.html',context)
#     elif request.method == 'POST':
#         id = request.POST.get('name')
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
    imageList = animal.image_set.all()
    context={'animal': animal, 'imageList': imageList}
    return render(request,'app01/showDetail.html',context)