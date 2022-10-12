from .serializers import *
from .models import *
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated


class SpecialisteLoginApi(APIView):
    def post(self,request):
        user = Specialiste.objects.all().filter(username=request.data['username']).first()
        if not user:
            raise APIException('Données invalides')        
        serializer = SpecialisteSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
""" 
class updatePassword(APIView):
    serializer_class = SpecialisteSerializer

    def post(self, request, *args, **kwargs):
        username = request.query_params["username"]
        if id != None:
            Spec = Specialiste.objects.get(username=username)
            serializer = SpecialisteSerializer(Spec, many = True)
            
            serializer.save(password=request.data)
            
            return Response(serializer.data)

"""




@api_view(["GET","POST"])
def view_api_ingredient(request):
    if request.method == "GET":
        queryset = Ingredient.objects.all()
        ser = IngredientSerializer(queryset, many = True)
        return Response(ser.data,status=status.HTTP_200_OK)
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
        return Response(ser.data,status=status.HTTP_200_OK)
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
def view_upload_dish(request):
    if request.method == 'POST':
        data = request.data
        ser = dishPicturesSerializer(data = data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)



@api_view(["GET","POST"])
def view_api_pays(request):
    if request.method == "GET":
        queryset = Pays.objects.all()
        ser = PaysSerializer(queryset, many = True)
        return Response(ser.data,status=status.HTTP_200_OK)

@api_view(["GET","POST"])
def view_photos_plats(request):
    if request.method == "GET":
        queryset = Plat.objects.all()
        ser = plat_image_serializer(queryset, many = True)
        return Response(ser.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        ser = plat_image_serializer(data = data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)



# Supprimer les 2 API ci-dessous
"""
@api_view(["POST"])
def view_api_publication_valide(request):
    data = request.data
    new_publication = Publication.objects.create(texte=data['texte'],photo=data['photo'],video=data['video'],heure_publication=data['heure_publication'],valide=1)
    user = Utilisateur.objects.get(id=data['user'])
    new_publication.user.add(user)
    ser = plat_image_serializer(data = new_publication)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(["POST"])
def view_api_publication_invalide(request):
    data = request.data
    new_publication = Publication.objects.create(texte=data['texte'],photo=data['photo'],video=data['video'],heure_publication=data['heure_publication'],valide=0)
    user = Utilisateur.objects.get(id=data['user'])
    new_publication.user.add(user)
    ser = plat_image_serializer(data = new_publication)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)
 """



# API de tweet (API pour le post d'un utilisateur)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_tweet(request):
    user = Utilisateur.objects.all().filter(username=request.data['tweep']).first() 
    if request.method == 'POST':
        files = request.FILES.getlist('file_content')
        if files:
            request.data.pop('file_content')
            serializer = TweetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(tweep=user)
                tweet_qs = Tweets.objects.get(id=serializer.data['id'])
                uploaded_files = []
                for file in files:
                    content = TweetFile.objects.create(tweep=user, media=file)
                    uploaded_files.append(content)

                tweet_qs.file_content.add(*uploaded_files)
                context = serializer.data
                context["file_content"] = [file.id for file in uploaded_files]
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TweetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(tweep=user)         
                context = serializer.data            
                return Response(context, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(serializer.errors, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#Pour consulter publication(get method) et la valider (post method)
class view_api_publication_valide(APIView):
    serializer_class = TweetSerializer

    def post(self, request, *args, **kwargs):
        id = request.query_params["id"]
        if id != None:
            tweet = Tweets.objects.get(id=id)
            tweet.valid = True
            tweet.save()
            serializer = TweetSerializer(tweet)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

#Pour consulter publication(get method) et la supprimer (post method)
class view_api_publication_invalide(APIView):
    serializer_class = TweetSerializer

    def post(self, request, *args, **kwargs):
        id = request.query_params["id"]
        if id != None:
            tweet = Tweets.objects.get(id=id)
            tweet.delete()
            
#Pour consulter toutes les publications non validées

@api_view(["GET"])
def view_api_publication_A_valider(request):
    liste = []
    queryset = Tweets.objects.all().filter(valid=False)
    for i in queryset.iterator():
        for j in list(i.file_content.all()):
            liste.append(j.media.name)
    print(liste)
    ser = TweetSerializer(queryset, many = True)
    return Response(ser.data,status=status.HTTP_200_OK)


class view_tweetFile(APIView):
    serializer = TweetFileSerializer
    def get(self, request, *args, **kwargs):    
        id = request.query_params["id"]
        if id != None:
            tweetFile = TweetFile.objects.all().filter(id=id)
            serializer = TweetFileSerializer(tweetFile, many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)

class view_tweeter(APIView):
    serializer = UtilisateurSerializer

    def get(self, request, *args, **kwargs):    
        first_name = request.query_params["first_name"]
        if first_name != None:
            User = Utilisateur.objects.all().filter(first_name=first_name)
            serializer = UtilisateurSerializer(User, many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)


class view_pub(APIView):
    serializer = TweetSerializer

    def get(self, request, *args, **kwargs):    
        id = request.query_params["id"]
        if id != None:
            tweet = Tweets.objects.all().filter(id=id)
            serializer = TweetSerializer(tweet, many = True)
            return Response(serializer.data,status=status.HTTP_200_OK)













