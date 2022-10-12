from .api import *
from django.urls import  path,re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('loginSpecialiste/', SpecialisteLoginApi.as_view(),name='loginSpecialiste' ),
    path('plat/', view_api_plat, name='plat'),
    path('pays/', view_api_pays,name='pays'),
    path('ingredient/', view_api_ingredient,name='ingredient'),
    path('food/', view_photos_plats,name='food'),
    path('pub_A_valider/', view_api_publication_A_valider,name='pub_A_valider'),
    path('pub_valide/', view_api_publication_valide.as_view(),name='pub_valide'),
    path('pub_invalide/', view_api_publication_invalide.as_view(),name='pub_invalide'),
    path('create_tweet/', create_tweet,name='create_tweet'),
    path('tweetFile/', view_tweetFile.as_view(),name='tweetFile'),
    path('tweeter/', view_tweeter.as_view(),name='tweeter'),
    path('consulterPub/', view_pub.as_view(),name='consulterPub'),  
    path('uploadImage/', view_upload_dish),   
   
] 