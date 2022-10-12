from django.db import models
import pickle

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

class Publication(models.Model):
    
    texte = models.CharField(max_length = 300)
    photo = models.ImageField()
    video = models.FileField()
    heure_publication = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey (Utilisateur,on_delete=models.CASCADE)
    valide =models.BooleanField(null=True)

    def __str__(self) -> str:
        return f"{self.Nom} {self.Description}"

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications" 


class TweetFile(models.Model):
    tweep =  models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    media = models.FileField(upload_to='images')

    def __str__(self):
        return f"{self.tweep.username}"
    
class photoPlat(models.Model):
    image = models.ImageField()

class Tweets(models.Model):
    texts = models.TextField()
    file_content = models.ManyToManyField(TweetFile, related_name='file_content', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    tweep = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    valid = models.BooleanField(null=True)
    class Meta:

        verbose_name_plural = 'Tweets'

    def __str__(self):
        return f"{self.texts}"








