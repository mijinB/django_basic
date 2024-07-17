from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestTweets(APITestCase):

    PAYLOAD = "Test Tweet"
    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(username="test", )
        user.set_password("123")
        user.save()
        self.user = user

        models.Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_get_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )

        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["payload"],
            self.PAYLOAD,
        )

    def test_create_tweet(self):
        new_tweet_payload = "New Tweet"

        response = self.client.post(
            self.URL,
            data={
                "payload": new_tweet_payload,
            },
        )
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)
        response = self.client.post(
            self.URL,
            data={
                "payload": new_tweet_payload,
            },
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(
            data["payload"],
            new_tweet_payload,
        )

        response = self.client.post(self.URL)
        self.assertEqual(response.status_code, 400)


class TestTweet(APITestCase):
    PAYLOAD = "Test Tweet"
    BASE_URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(username="test", )
        user.set_password("123")
        user.save()
        self.user = user

        models.Tweet.objects.create(
            payload=self.PAYLOAD,
            user=self.user,
        )

    def test_tweet_not_found(self):
        response = self.client.get(f"{self.BASE_URL}2")
        self.assertEqual(response.status_code, 404)

    def test_get_tweet(self):
        response = self.client.get(f"{self.BASE_URL}1")
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertEqual(
            data["payload"],
            self.PAYLOAD,
        )

    def test_put_tweet(self):
        self.client.force_login(self.user)
        response = self.client.put(
            f"{self.BASE_URL}1",
            data={
                "payload": self.PAYLOAD,
            },
        )
        self.assertEqual(response.status_code, 200)

        response = self.client.put(
            f"{self.BASE_URL}1",
            data={
                "payload": "",
            },
        )
        self.assertEqual(response.status_code, 400)

    def test_delete_tweet(self):
        self.client.force_login(self.user)
        response = self.client.delete(f"{self.BASE_URL}1")
        self.assertEqual(response.status_code, 200)
