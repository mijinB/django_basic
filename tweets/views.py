from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer


@api_view()
def tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(
        tweets,
        many=True,
    )
    return Response(
        {
            "ok": True,
            "tweets": serializer.data,
        }
    )
