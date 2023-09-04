from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy




# Create your views here.
def inicio(request):
    return render(request, "app/inicio.html")

def registrate(request):
    return render(request, "app/registrate.html",)

@login_required
def comprar(request):
    return render(request, "app/comprar.html")

@login_required
def vender(request):
    return render(request, "app/vender.html")

@login_required
def catalogo(request):
    contexto = {'piezas': Oleo.objects.all() }
    return render(request, "app/catalogo.html", contexto)

def acercaDeMi(request):
    return render(request, "app/acercaDeMi.html")







#Buscar
@login_required
def buscarOleo(request):
    return render(request, "app/buscarOleo.html")

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        nombre = Oleo.objects.filter(nombre__icontains=patron)
        contexto = {"oleo_list": nombre}
        return render(request, "app/oleo_list.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

@login_required
def buscarAcuarela(request):
    return render(request, "app/buscarAcuarela.html")

@login_required
def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        nombre = Acuarela.objects.filter(nombre__icontains=patron)
        contexto = {"acuarela_list": nombre}
        return render(request, "app/acuarela_list.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

@login_required
def buscarCarboncillo(request):
    return render(request, "app/buscarCarboncillo.html")

@login_required
def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        nombre = Carboncillo.objects.filter(nombre__icontains=patron)
        contexto = {"carboncillo_list": nombre}
        return render(request, "app/carboncillo_list.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")


#Login
def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")
            user = authenticate(username=usuario, password=password )
            if user is not None:
                login(request, user)
                return render(request, "app/inicio.html", {'mensaje': f'Bienvenido'})
            else: 
                return render(request, "app/login.html", {'form': formulario, 'mensaje':"Usuario o contrasenia no validos, revise su informacion"})
        else:
            return render(request, "app/login.html", {'form': formulario, 'mensaje':"Usuario o contrasenia no validos, revise su informacion"})

    formulario = AuthenticationForm()

    return render(request, "app/login.html", {"form":formulario})

def registrar(request):
    if request.method == "POST":
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            formulario.save()
            return render(request, "app/login.html")
    else:
        formulario = RegistroForm()
    return render(request, "app/registro.html", {"form":formulario})

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST)

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"app/inicio.html")
        else:
            return render(request,"app/editarUsuario.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "app/editarUsuario.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

           
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()   

            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"app/inicio.html")
    else:
        form = AvatarForm()
    return render(request, "app/agregarAvatar.html", {'form': form })

#Clases
class OleoCrear(CreateView):
    model = Oleo
    fields = ['nombre',
              'descripcion',
              'precio',
              'dimensiones',
              'imagenOleo']
    success_url = reverse_lazy('inicio')


class AcuarelaCrear(CreateView):
    model = Acuarela
    fields = ['nombre',
              'descripcion',
              'precio',
              'dimensiones',
              'imagenAcuarela']
    success_url = reverse_lazy('inicio')


class CarboncilloCrear(CreateView):
    model = Carboncillo
    fields = ['nombre',
              'descripcion',
              'precio',
              'dimensiones',
              'imagenCarboncillo']
    success_url = reverse_lazy('inicio')

#catalogo
class OleoList(ListView):
    model = Oleo

class AcuarelaList(ListView):
    model = Acuarela

class CarboncilloList(ListView):
    model = Carboncillo

#editar productos
class OleoEditar(UpdateView):
    model = Oleo
    fields = ['nombre',
              'descripcion',
              'precio']
    success_url = reverse_lazy('inicio')

class AcuarelaEditar(UpdateView):
    model = Acuarela
    fields = ['nombre',
              'descripcion',
              'precio']
    success_url = reverse_lazy('inicio')

class CarboncilloEditar(UpdateView):
    model = Carboncillo
    fields = ['nombre',
              'descripcion',
              'precio']
    success_url = reverse_lazy('inicio')

#borrar productos
class OleoBorrar(DeleteView):
    model = Oleo
    success_url = reverse_lazy('inicio')

class AcuarelaBorrar(DeleteView):
    model = Acuarela
    success_url = reverse_lazy('inicio')

class CarboncilloBorrar(DeleteView):
    model = Carboncillo
    success_url = reverse_lazy('inicio')


