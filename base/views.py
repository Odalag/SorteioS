from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Profile


class HomeView(TemplateView):
    template_name = 'home.html'

class SobreView(TemplateView):
    template_name = 'sobre.html'

def register(request):
    if request.method == 'GET':
        return render(request, "cadastro.html")

    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        telefone = request.POST.get('telefone')
        matricula = request.POST.get('matricula')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        profile = Profile.objects.create(matricula=matricula, telefone=telefone, user=user)
        profile.save()
        return render(request, "login.html")

def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login_django(request, user)
            #return render(request, "home.html") 
            return HttpResponseRedirect(reverse('home')) 
        
        else:
           return HttpResponseRedirect(reverse('login')) 
