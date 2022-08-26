from .api import SpecialisteLoginApi,view_photos_plats,view_photos_plats,view_api_pays,view_api_ingredient,view_api_plat
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('loginSpecialiste/', SpecialisteLoginApi.as_view() ),
    path('plat/', view_api_plat),
    path('pays/', view_api_pays),
    path('ingredient/', view_api_ingredient),
    path('food/', view_photos_plats),
] 