from django.db import models
from tweets.models import Tweet

class Usuario(models.Model):
    i_d = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 80)
    userName = models.CharField(max_length = 40)
    resena = models.CharField(max_length=80, blank  =  True)
    password = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 240)
    imagenPerfil = models.ImageField(upload_to="perfil",default = "perfil/default.jpg")
    imagenPortada = models.ImageField(upload_to="portada",default = "portada/default.jpg")
    siguiendo = models.ManyToManyField('self',blank = True)
    numeroSiguiendo = models.IntegerField(default = 0)
    seguidores = models.ManyToManyField('self',blank = True)
    numeroSeguidores = models.IntegerField(default = 0)
    tweets = models.ManyToManyField(Tweet,blank=True)
    
    def __str__(self):
        return self.userName
    
    