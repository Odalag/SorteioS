from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'home.html'

class LoginView(TemplateView):
    template_name = 'login.html'

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
        aluno = request.POST.get('aluno')
        checkbox = request.POST.get('checkbox')

        #user = User.objects.filter('username').first()

        #if user:
        #    return render(request, "core/pages/permisson.html")
        #else:
        user = User.objects.create_user(username=username, email=email, password=password, telefone=telefone, aluno=aluno, checkbox=checkbox)

        return render(request, "home.html")
