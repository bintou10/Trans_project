from django.test import SimpleTestCase
from django.urls import reverse,resolve
from foodApp.api import *


class TestUrls(SimpleTestCase):

    def test_loginSpecialiste_url_resolves(self):
        url = reverse('loginSpecialiste')
        self.assertEquals(resolve(url).func.view_class,SpecialisteLoginApi)

    def test_plat_url_resolves(self):
        url = reverse('plat')
        self.assertEquals(resolve(url).func,view_api_plat)

    def test_pays_url_resolves(self):
        url = reverse('pays')
        self.assertEquals(resolve(url).func,view_api_pays)

    def test_ingredient_url_resolves(self):
        url = reverse('ingredient')
        self.assertEquals(resolve(url).func,view_api_ingredient)

    def test_food_url_resolves(self):
        url = reverse('food')
        self.assertEquals(resolve(url).func,view_photos_plats)

    def test_pub_A_valider_url_resolves(self):
        url = reverse('pub_A_valider')
        self.assertEquals(resolve(url).func,view_api_publication_A_valider)

    def test_pub_valide_url_resolves(self):
        url = reverse('pub_valide')
        self.assertEquals(resolve(url).func.view_class,view_api_publication_valide)

    def test_pub_invalide_url_resolves(self):
        url = reverse('pub_invalide')
        self.assertEquals(resolve(url).func.view_class,view_api_publication_invalide)

    def test_create_tweet_url_resolves(self):
        url = reverse('create_tweet')
        self.assertEquals(resolve(url).func,create_tweet)


    def test_tweetFile_url_resolves(self):
        url = reverse('tweetFile')
        self.assertEquals(resolve(url).func.view_class,view_tweetFile)

    def test_tweeter_url_resolves(self):
        url = reverse('tweeter')
        self.assertEquals(resolve(url).func.view_class,view_tweeter)

    def test_consulterPub_url_resolves(self):
        url = reverse('consulterPub')
        self.assertEquals(resolve(url).func.view_class,view_pub)
        