from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class ContactView(TemplateView):
    template_name = 'contact.html'


