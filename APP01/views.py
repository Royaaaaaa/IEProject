from django.shortcuts import render

from django.http import *

from .models import *

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

def showDetail(request,id):
    image = Image.objects.get(pk=id)
    animal = image.iAnimal
    context={'animal': animal}
    return render(request,'app01/showDetail.html',context)