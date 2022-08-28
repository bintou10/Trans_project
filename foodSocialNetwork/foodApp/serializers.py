
from rest_framework import serializers
from .models import  Specialiste,Ingredient,Plat,Pays,Publication



class SpecialisteSerializer(serializers.ModelSerializer):
    pays = serializers.StringRelatedField()
    class Meta:
        model =  Specialiste
        fields = ( 'id','first_name', 'last_name','username' ,'nationalite' , 'pays','photo' )

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = "__all__"

class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = "__all__"

class plat_image_serializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = ('photo',)

class publications_serializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = "__all__"





      
