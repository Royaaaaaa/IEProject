from django.db import models

class Type(models.Model):
    tName = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.tName

class Animal(models.Model):
  aName=models.CharField(max_length=28)
  aType=models.ForeignKey(Type,on_delete=models.CASCADE)
  aHabitat=models.CharField(max_length=40)
  aSize=models.CharField(max_length=20)
  aDetail=models.CharField(max_length=10000,default='hhhh')


  def __str__(self):
      return self.aName

class Image(models.Model):
    iName=models.CharField(max_length=20)
    iAnimal=models.ForeignKey(Animal,on_delete=models.CASCADE)

class Location(models.Model):
    latAnimal = models.FloatField(null=True, blank=True,default=None)
    lonAnimal = models.FloatField(null=True, blank=True,default=None)
    lAnimal=models.ForeignKey(Animal,on_delete=models.CASCADE)
