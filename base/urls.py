from ast import increment_lineno
from django.http import HttpResponse
from django.urls import path
from .views import HomeView, LoginView, ContactView

urlpatterns = [
    path("home/", HomeView.as_view()),
    path("login/", LoginView.as_view()),
    path("contacts/", ContactView.as_view())
]