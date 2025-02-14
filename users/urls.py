from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("password", views.ChangePassword.as_view()),
    path("login", views.Login.as_view()),
    path("logout", views.Logout.as_view()),
    path("<int:pk>", views.UserDetail.as_view()),
    path("<int:pk>/tweets", views.UserTweets.as_view()),
]
