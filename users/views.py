from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


class UserTweets(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
