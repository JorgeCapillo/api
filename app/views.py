from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from usuarios.models import *
from usuarios.models import *
# Create your views here.

@csrf_exempt
def usuarios(request):
    try:
        cookie = request.COOKIES['sessionid']
        login = {"id":request.session['user_id'],"login":request.session['login']}
    except:
        login = False
    usuarios = Usuario.objects.all().values()
    return render_to_response('usuarios.html',{"usuarios":usuarios,"login":login})


def home(request):
    try:
        if(request.COOKIES['sessionid']):
            login = request.session['login']
            if(login == False):
                return render_to_response('home.html')
            else:
                user = Usuario.objects.filter(i_d=request.session["user_id"]).values()
                return render_to_response('login.html',{"user":user[0]})
    except:
        return render_to_response('home.html')