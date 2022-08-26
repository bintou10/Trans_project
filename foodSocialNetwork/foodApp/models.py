from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    
    nationalite = models.CharField(max_length=100)
    photo = models.ImageField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

class Pays(models.Model):
    
    nom = models.CharField(max_length=300)
    drapeau = models.ImageField()

    def __str__(self) -> str:
        return f"{self.nom} "
    class Meta:
        verbose_name = "Pays"


class Specialiste(Utilisateur):
    pays = models.ForeignKey(Pays,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "Spécialiste"
        verbose_name_plural = "Spécialistes"

class Ingredient(models.Model):
    
    Nom = models.CharField(max_length=300)
    Description =  models.TextField(max_length=300)
    Photo = models.ImageField()

    def __str__(self) -> str:
        return f"{self.Nom} "

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients" 

class Plat(models.Model):
    
    nom = models.CharField(max_length=300)
    description = models.TextField(max_length=300)
    photo = models.ImageField()
    plat_national = models.BooleanField(null=True)
    pays = models.ManyToManyField(Pays)
    ingredients = models.ManyToManyField(Ingredient)
    recette = models.TextField(max_length=50000)

    def __str__(self) -> str:
        return f"{self.nom} "

    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats" 






