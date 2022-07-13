from ast import increment_lineno
from django.http import HttpResponse
from django.urls import path
from .views import view_home, view_about, view_contacts

urlpatterns = [
    path("home/", view_home),
    path("about/", view_about),
    path("contacts/", view_contacts)
]