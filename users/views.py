from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from tweets.models import Tweet
from .models import User
from tweets.serializers import TweetSerializer


@api_view()
def userTweets(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise NotFound

    tweets = Tweet.objects.filter(user=user)
    serializer = TweetSerializer(
        tweets,
        many=True,
    )
    print(serializer.data)
    return Response(
        {
            "ok": True,
            "user": user.username,
            "tweets": serializer.data,
        }
    )
