from ast import increment_lineno
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, LoginView, SobreView, register

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("sobre/", SobreView.as_view(), name='sobre'),
    path('login/', LoginView.as_view(), name="login"),
    path('cadastro/', register, name = 'cadastro'),
]