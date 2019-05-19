from django.db import models

class Type(models.Model):
    tName = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.tName

class Size(models.Model):
    sName = models.CharField(max_length=20)

    def __str__(self):
        return self.sName

class Color(models.Model):
    cName = models.CharField(max_length=20)
    def __str__(self):
        return self.cName

class Animal(models.Model):
  aName=models.CharField(max_length=28)
  aType=models.ForeignKey(Type,on_delete=models.CASCADE,default=None)
  aSize=models.ForeignKey(Size,on_delete=models.CASCADE,default=None)
  aColor=models.ForeignKey(Color,on_delete=models.CASCADE,default=None)
  aFamily=models.CharField(max_length=50,default='')
  aFact=models.CharField(max_length=1000, default="")
  aWeight=models.CharField(max_length=28,default="")
  aLength = models.CharField(max_length=28,default="")
  aLifespan = models.CharField(max_length=50,default="")
  aFeature = models.CharField(max_length=1000,default="")
  aPopulation = models.IntegerField(null=True, blank=True, default=None)


  def __str__(self):
      return self.aName

# class Image(models.Model):
#     iName=models.CharField(max_length=50)
#     iAnimal=models.ForeignKey(Animal,on_delete=models.CASCADE)

class Location(models.Model):
    latAnimal = models.FloatField(null=True, blank=True,default=None)
    lonAnimal = models.FloatField(null=True, blank=True,default=None)
    lAnimal=models.ForeignKey(Animal,on_delete=models.CASCADE)

class Score(models.Model):
    score = models.IntegerField()

    def __str__(self):
        return self.score