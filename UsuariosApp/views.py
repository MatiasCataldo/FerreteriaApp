from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from UsuariosApp.forms import FormularioRegistro, FormularioEdicionPerfil
from django.contrib.auth.decorators import login_required
from UsuariosApp.models import InfoExtra


def login(request):  
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            django_login(request, usuario)
            InfoExtra.objects.get_or_create(user=usuario)
            return redirect("inicio")
    else:
        formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario': formulario})


def registro(request):
    if request.method == "POST":
        print("Entro al if")
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            InfoExtra.objects.get_or_create(user=usuario)
            return redirect("login")
        else:
            return render(request, 'usuarios/registro.html', {
                'formulario': formulario,
                'errores': formulario.errors
            })
    else:
        formulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})


@login_required
def editar_perfil(request):
    infoextra = request.user.infoextra
    if request.method == "POST":
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():  
            if formulario.cleaned_data.get('avatar'):
                infoextra.avatar = formulario.cleaned_data.get('avatar')
            if formulario.cleaned_data.get('fechaNacimiento'):
                infoextra.fechaNacimiento = formulario.cleaned_data.get('fechaNacimiento')
            infoextra.save()
            formulario.save()
            return redirect("perfil_usuario")
    else:
        formulario = FormularioEdicionPerfil(initial={'avatar': infoextra.avatar}, instance=request.user)
    return render(request, "usuarios/editar_perfil.html", {'formulario': formulario})
    

@login_required
def perfil_usuario(request):
    infoextra = request.user.infoextra
    user = request.user
    return render(request, "usuarios/perfil_usuario.html", {'infoextra': infoextra, 'user': user})
