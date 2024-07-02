from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("elon musk", "Elon Musk"),
            ("! elon musk", "! Elon Musk"),
        ]

    def queryset(self, request, tweets):
        word = self.value()
        if word:
            if word.startswith("!"):
                return tweets.exclude(payload__icontains=word[2:])
            else:
                return tweets.filter(payload__contains=word)
        else:
            tweets


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "payload",
        "user",
        "number_of_likes",
        "created_at",
    )
    list_filter = (
        WordFilter,
        "created_at",
    )
    search_fields = (
        "payload",
        "user__name",
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "user",
        "tweet",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = ("user__name",)
