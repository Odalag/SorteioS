from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
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
        checkbox = request.POST.get('checkbox')

        #user = User.objects.filter('username').first()

        #if user:
        #    return render(request, "core/pages/permisson.html")
        #else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        Profile.objects.create(telefone=telefone, user=user, matricula=matricula)
        return render(request, "home.html")

def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(email=email, password=password)
        
        if user is not None:
            login_django(request, user)
            return render(request, "home.html") 
            
        else:
           return render(request, "login.html")
