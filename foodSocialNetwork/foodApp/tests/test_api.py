
from django.test import Client
import unittest
from foodApp.api import *
from rest_framework import status
from django.urls import reverse



class TestApis(unittest.TestCase):

    def test_SpecialisteLoginApi_should_log_PapaGastro(self):
        client = Client()
        data = {
            "username" : "PapaGastro",
            "password" : "Gpapa001",
        }
        url = reverse('loginSpecialiste')
        resp = client.post(url,data=data,format="json")
        self.assertEqual(resp.status_code,status.HTTP_200_OK)

    def test_plat_should_show_all_dishes(self):
        client = Client()
        url = reverse('plat')
        response = client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_ingredient_should_show_all_dishes(self):
        client = Client()
        url = reverse('ingredient')
        response = client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_pays_should_show_all_coutries(self):
        client = Client()
        url = reverse('pays')
        response = client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_pays_should_show_all_foods(self):
        client = Client()
        url = reverse('food')
        response = client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_pays_should_show_all_post_needed_to_be_validated(self):
        client = Client()
        url = reverse('pub_A_valider')
        response = client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_tweetFile_should_show_tweetFile_with_id_equal_to_11(self):
        client = Client()
        resp = client.get('%s?id=%s' % (reverse('tweetFile'), '11'))
        self.assertEqual(resp.status_code,status.HTTP_200_OK)

    def test_tweeter_should_show_tweeter_Adji_Diouf_data(self):
        client = Client()
        resp = client.get('%s?first_name=%s' % (reverse('tweeter'), 'Adji'))
        self.assertEqual(resp.status_code,status.HTTP_200_OK)

    def test_consulterPub_should_show_post_with_id_equal_to_11(self):
        client = Client()
        resp = client.get('%s?id=%s' % (reverse('consulterPub'), '11'))
        self.assertEqual(resp.status_code,status.HTTP_200_OK)
        
    def test_create_tweet_should_create_tweet(self):
        pass
        
#ca marche mais essayer avec un autre id où valid est à false
""" 
    def test_pub_valide_should_set_valid_to_true_in_post_with_id_equal_to_11(self):
        client = Client()
        resp = client.post('%s?id=%s' % (reverse('pub_valide'), '11'))
        self.assertEqual(resp.status_code,status.HTTP_202_ACCEPTED)
"""
    #pas encore testé mais essayer avec un autre id qui existe et qu'on veut supprimer
""" 
    def test_pub_invalide_should_delete_post_with_id_equal_to_11(self):
        client = Client()
        resp = client.post('%s?id=%s' % (reverse('pub_invalide'), '11'))
        self.assertIsNone(resp)
"""




    




        



