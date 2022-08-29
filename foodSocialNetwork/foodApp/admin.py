

# Register your models here.
from django.contrib import admin
from .models import TweetFile,Tweets,Pays,Utilisateur,Specialiste,Ingredient,Plat,Publication

# Register your models here.
admin.site.register(Pays)
admin.site.register(Utilisateur)
admin.site.register(Specialiste)
admin.site.register(Ingredient)
admin.site.register(Plat)
admin.site.register(Publication)
admin.site.register(Tweets)
admin.site.register(TweetFile)

