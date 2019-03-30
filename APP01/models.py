from django.db import models

class Type(models.Model):
    tName = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)

class Animal(models.Model):
  aName=models.CharField(max_length=28)
  aType=models.ForeignKey(Type,on_delete=models.CASCADE)
  aHabitat=models.CharField(max_length=40)
  aSize=models.CharField(max_length=20)


  def __str__(self):
      return self.aName

class Image(models.Model):
    iName=models.CharField(max_length=20)
    iAnimal=models.ForeignKey(Animal,on_delete=models.CASCADE)