from django.shortcuts import render_to_response, redirect
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
            request.session['user_id'] = nuevo.i_d
            request.session['login'] = True
            return HttpResponse("User Created")
    else:
        return redirect('home')

@csrf_exempt
def eliminarUser(request):
    if request.method == "GET":
        try:
            if(request.COOKIES['sessionid']):
                login = request.session['login']
                if(login == True):
                    usuario = Usuario.objects.get(i_d=request.session['user_id'])
                    usuario.delete()
                    request.session['login']=False
                    request.session['user_id']=0
            return redirect('home')       
        except:
             return redirect('home') 
        return redirect('home')
    else:
        return HttpResponse("¿?")
    
@csrf_exempt
def salir(request):
    try:
        if(request.COOKIES['sessionid']):
            request.session['login']=False
            request.session['user_id']=0
            return redirect('home')
    except:
        return redirect('home')
            
        
def login(request):
    if request.method == "POST":
        post = request.body.decode()
        post = json.loads(post)
        usuario = (Usuario.objects.filter(email=post['email']).count() > 0)
        if(usuario):
            usuario = Usuario.objects.get(email=post['email'])
            if (post['password']==usuario.password):
                request.session['user_id'] = usuario.i_d
                request.session['login'] = True
                return HttpResponse("Logged User")
            else:
                return HttpResponse("Invalid Password")
        else:
            return HttpResponse("Invalid Email")
    else:
        return redirect ('home')
    