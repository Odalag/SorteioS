from ast import increment_lineno
from django.http import HttpResponse
from django.urls import path
from .views import HomeView, LoginView, SobreView

urlpatterns = [
    path("", HomeView.as_view()),
    path("login/", LoginView.as_view()),
    path("sobre/", SobreView.as_view())
]