from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#criar modo

# class Users(models.Model):
#     nome = models.CharField('Nome', max_length=50)
#     telefone = models.CharField('Telefone', max_length=20)
#     email = models.CharField('Email', max_length=100)
#     senha = models.CharField('Senha', max_length=8)

class Profile(models.Model):
    telefone = models.CharField('Telefone', max_length=20, null=True, blank=True)
    matricula = models.CharField('Matricula', max_length=14, null=True, blank=True)
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username