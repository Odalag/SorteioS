from django.http import HttpResponse
from django.shortcuts import render


def view_home(request):
    return HttpResponse("Pagina Home")

def view_about(response):
    return HttpResponse("Pagina About")

def view_contacts(response):
    return HttpResponse("Pagina Contacts")
