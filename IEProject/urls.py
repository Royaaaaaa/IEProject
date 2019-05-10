"""IEProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from APP01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^index',views.index),
    url(r'^marinefamily$',views.marinefamily),
    url(r'^quiz$',views.quiz),
    # url(r'^game$',views.game),
    # url(r'^storyAndFact$',views.storyAndFact),
    url(r'^search$',views.advsearch),
    # url(r'^searchtype$',views.searchtype),
    url(r'advsearch-(?P<aType_id>(\d+))-(?P<aColor_id>(\d+))-(?P<aSize_id>(\d+))', views.advsearch),
    # url(r'^search?type=(?P<type_id>(\d+))&size=(?P<size_id>(\d+))&colour=(?P<colour_id>(\d+))$', views.advsearch),
    # url(r'getimg', views.getimg),
    url(r'^(\d+)$',views.showDetail),
    url(r'^typeid=(\d+)$',views.marinelife),
    url(r'^pickingrubbish',views.pickingrubbish),
    url(r'^puzzle',views.puzzle),
    url(r'^nearbyAnimal',views.findNearbyAnimals),
    url(r'^savescore',views.score)
    # url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'/static/'}),


]
