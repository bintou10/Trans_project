
from rest_framework import serializers
from .models import  photoPlat,Utilisateur,Tweets,Specialiste,Ingredient,Plat,Pays,Publication,TweetFile



class SpecialisteSerializer(serializers.ModelSerializer):
    pays = serializers.StringRelatedField()
    class Meta:
        model =  Specialiste
        fields = ( 'id','first_name', 'last_name','username' ,'nationalite' , 'pays','photo' )

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Utilisateur
        fields = "__all__"

class dishPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = photoPlat
        fields = "__all__"


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
    
class TweetFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetFile
        fields = "__all__"

class TweetSerializer(serializers.ModelSerializer):
    tweep = serializers.StringRelatedField()


    class Meta:
        model = Tweets
        fields = ['id', 'texts', 'file_content', 'date_posted', 'tweep','valid']
        extra_kwargs = {
            "file_content": {
                "required": False,
            }
        }
   





      
