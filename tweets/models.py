from django.db import models
from usuarios.models import *
# Create your models here.
class Tweet(models.Model):
    i_dT = models.AutoField(primary_key=True)
    contenido = models.TextField(max_length = 140)
    nombreUser = models.CharField(max_length=80)
    apellidoUser = models.CharField(max_length = 80)
    nickUser = models.CharField(max_length = 40)
    imgUser = models.ImageField(upload_to="tweets/perfil")
    favoritos = models.IntegerField(default = 0)
    retweets = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.nick