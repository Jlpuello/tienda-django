from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

#from django.contrib.auth.models import User
from users.models import User

from .forms import RegisterForm
from products.models import Products


def Index(request):

    products = Products.objects.all().order_by('-id')

    return render(request,'index.html',{
        'message':'Andrea Store',
        'title':'productos',
        'products': products,
    })


def loginviews(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request,'Usuario o contraseña no validos')

    return render(request,'user/login.html',{
            
        })

def logoutviews(request):
    logout(request)
    messages.success(request,'secion cerrada satisfactoriamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form=RegisterForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
       
        user = form.save()
        if user:
            login(request,user)
            messages.success(request,'Usuario Creado Exitosamente')
            return redirect('index')
        
    return render(request,'user/register.html',{
    'form':form
    })