from ast import increment_lineno
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, LoginView, SobreView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("sobre/", SobreView.as_view(), name='sobre'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]