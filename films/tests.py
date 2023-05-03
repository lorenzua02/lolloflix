from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from films.models import Film


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "lmogicato",
            "email": "lorenzo.mogicato@gmail.com",
            "password": "godohoPyCharmPROgratis#0362",
            "re_password": "godohoPyCharmPROgratis#0362",
        }
        response = self.client.post("/auth/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReviewTestCase(APITestCase):
    film_list_url = reverse("film-list")

    def setUp(self):
        self.user = User.objects.create_user(username="lollomogicato0362", password="t1zi4noF3RR0@xyz")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_seen_flag(self):
        Film.objects.create(title="The Imitation Game", release_year=2014, platform="Netflix")

        response = self.client.get(self.film_list_url, kwargs={"pk": 1})
        self.assertEqual(False, response.json()[0]["seen"])

        self.client.post(
            reverse("film-review", kwargs={"film_pk": 1}),
            {"vote": 9, "comment": "bu bu milano"}
        )
        response = self.client.get(self.film_list_url, kwargs={"pk": 1})
        self.assertEqual(True, response.json()[0]["seen"])

    def test_user_detail_retrieve(self):
        response = self.client.get(reverse("user-detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "lollomogicato0362")
