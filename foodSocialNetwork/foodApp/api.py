from .serializers import SpecialisteSerializer,plat_image_serializer,IngredientSerializer,PlatSerializer,PaysSerializer

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .models import Specialiste,Ingredient,Plat,Pays


class SpecialisteLoginApi(APIView):
    def post(self,request):
        user = Specialiste.objects.all().filter(username=request.data['username']).first()
        if not user:
            raise APIException('Données invalides')        
        serializer = SpecialisteSerializer(user)
        return Response(serializer.data)


@api_view(["GET","POST"])
def view_api_ingredient(request):
    if request.method == "GET":
        queryset = Ingredient.objects.all()
        ser = IngredientSerializer(queryset, many = True)
        return Response(ser.data)
    elif request.method == 'POST':
        data = request.data
        ser = IngredientSerializer(data = data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)


@api_view(["GET","POST"])
def view_api_plat(request):
    if request.method == "GET":
        queryset = Plat.objects.all()
        ser = PlatSerializer(queryset, many = True)
        return Response(ser.data)
    elif request.method == 'POST':
        data =request.data
        new_plat = Plat.objects.create(nom=data['nom'],description=data['description'],photo=data['photo'],plat_national=data['plat_national'],recette=data['recette'])
        for p in data['pays']:
            pays_obj = Pays.objects.get(id=p)
            new_plat.pays.add(pays_obj)
        for ing in data['ingredients']:
            ing_obj = Ingredient.objects.get(id=ing)
            new_plat.ingredients.add(ing_obj)
        ser = PlatSerializer(data = new_plat)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)

@api_view(["GET","POST"])
def view_api_pays(request):
    if request.method == "GET":
        queryset = Pays.objects.all()
        ser = PaysSerializer(queryset, many = True)
        return Response(ser.data)

@api_view(["GET","POST"])
def view_photos_plats(request):
    if request.method == "GET":
        queryset = Plat.objects.all()
        ser = plat_image_serializer(queryset, many = True)
        return Response(ser.data)
    elif request.method == 'POST':
        data = request.data
        ser = plat_image_serializer(data = data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)










