from django.contrib import admin
from .models import *

# class imageInline(admin.StackedInline):
#     model = Image
#     extro = 3

class locationInline(admin.StackedInline):
    model = Location
    extro = 4

class animalInline(admin.StackedInline):
    model = Animal
    extro = 3

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id','aName']
    search_fields = ['aName']
    list_filter = ['aName']
    list_per_page = 20
    # inlines = [imageInline]
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['id','score']

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['id','iName']
#     search_fields = ['iName']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','latAnimal','lonAnimal','lAnimal']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','tName']
    search_fields = ['tName']
    inlines = [animalInline]

class SizeAdmin(admin.ModelAdmin):
    list_display = ['id','sName']
    inlines = [animalInline]

class ColorAdmin(admin.ModelAdmin):
    list_display = ['id','cName']
    inlines = [animalInline]

admin.site.register(Animal,AnimalAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Score,ScoreAdmin)
admin.site.register(Location,LocationAdmin)
