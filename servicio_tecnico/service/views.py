from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def panel_de_control(request):
    return render(request, 'panel_de_control.html')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user)

        if user is None:
            return render(request, 'login.html', {
                'error': 'usuario y/o contraseña incorrectos, verifique los datos ingresados'
            })
        else:
            login(request, user)
            return redirect('panelPC')

def registrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'registro_usuario.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return render(request, 'login.html', {'mensaje': 'Cuenta creada con exito, puede loguearse'})
            except:
                return render(request, 'registro_usuario.html', {'error':'El usuario ingresado ya existe'})
        else:
            return render(request, 'registro_usuario.html', {'error':'Las contraseñas no coinciden'})
        
def datos_usuario(request):
    return render(request, 'datos_usuario.html')

