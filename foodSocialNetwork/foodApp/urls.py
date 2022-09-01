from .api import *
from django.urls import  path,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('loginSpecialiste/', SpecialisteLoginApi.as_view() ),
    path('plat/', view_api_plat),
    path('pays/', view_api_pays),
    path('ingredient/', view_api_ingredient),
    path('food/', view_photos_plats),
    path('pub_A_valider/', view_api_publication_A_valider),
    path('pub_valide/', view_api_publication_valide.as_view()),
    path('pub_invalide/', view_api_publication_invalide.as_view()),
    path('create_tweet/', create_tweet),
    path('tweetFile/',  view_tweetFile.as_view()),
   
    
] 