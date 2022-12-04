from ast import increment_lineno
from django.http import HttpResponse
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from .views import HomeView, login, SobreView, register

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("sobre/", SobreView.as_view(), name='sobre'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', register, name='cadastro'),
]