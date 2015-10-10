from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from usuarios.models import *
# Create your views here.

@csrf_exempt
def crearUser(request):
    if request.method == "POST":
        post = request.body.decode()
        post = json.loads(post)
        userName = (Usuario.objects.filter(userName=post['userName']).count() > 0)
        email = (Usuario.objects.filter(email=post['email']).count() > 0)
        if(userName):
            return HttpResponse("Inavalid UserName")
        else:
            if(email):
                return HttpResponse("Invalid Email")
            else:
                nuevo = Usuario(name=post['name'],userName=post['userName'],password=post['password'],email=post['email'])
            nuevo.save()
            request.session["user_id"] = nuevo.i_d
            request.session["login"] = True
            return HttpResponse("User Created")
    else:
        return redirect('home')


def eliminarUser(request,user):
    if request.method == "GET":
        usuario = Usuario.objects.get(i_d=user)
        usuario.delete()
    return redirect('usuarios')
    
def salir(request):
    try:
        if(request.COOKIES['sessionid']):
            request.session['login']=False
            request.session['user_id']=0
            return redirect('home')
    except:
        return redirect('home')
            