from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import OsCabecalho
from django.contrib.auth import authenticate, login as djangologin,logout as djangologout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def home(request):
    franklyn = 'gostoso'
    print(request.user.first_name)
    os = OsCabecalho.objects.all()
    return render(request,'gos/paginas/teste.html',{'franklyn' : franklyn,
    'os' : os})

def consulta(request,osservico):
    os = OsCabecalho.objects.get(servico=osservico)
    return render(request,'gos/cabecalho.html',{'os' : os})

def login (request):
#-----------------------------------------
# este metodo verifica se esta auth = request.user.is_authenticated()

    next = request.GET.get('next')
    if request.method != 'POST':
        return render(request,'gos/paginas/login.html',{'next':next})    
    username = request.POST.get('username')    
    password = request.POST.get('password')
    next     = request.POST.get('next')
    print(request.POST)
    user = authenticate(username=username,password =password)
    if user:  #reforçar futuramente a segurança
        djangologin(request,user)
        if next:
            #return HttpResponse('algo') 
            return HttpResponseRedirect(next)        
        return HttpResponseRedirect('/admin/')
    if not user:
        return HttpResponse('algo deu errado')
            


def getlogin (request):
    pass        

def logout (request):
    djangologout(request)
    return HttpResponseRedirect('/login/')