from django.shortcuts import render

from django.http import *

from .models import *

def index(request):
    return render(request,'app01/index.html')
