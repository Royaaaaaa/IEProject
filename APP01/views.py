from django.shortcuts import render

from django.http import *

from .models import *

def index(request):
    return render(request,'app01/index.html')
def marinelife(request):
    return render(request,'app01/marinelife.html')
def recyclevideo(request):
    return render(request,'app01/recyclevideo.html')
def game(request):
    return render(request,'app01/game.html')
def aboutUs(request):
    return render(request,'app01/aboutUs.html')