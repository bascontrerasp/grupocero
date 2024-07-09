from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Ciudad,Cliente
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password,check_password
from .forms import CiudadForm
import re
from django.contrib import messages

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

# Create your views here.

def base(request):
    context={}
    return render(request, 'aplicacion/base.html')

def index(request):
    return render(request, 'aplicacion/index.html')

def formulario(request):
    context={}
    return render(request, 'aplicacion/formulario.html')

def catalogo(request):
    context={}
    return render(request, 'aplicacion/catalogo.html')

def tienda(request):
    context={}
    return render(request, 'aplicacion/tienda.html')

def terminos(request):
    context={}
    return render(request, 'aplicacion/terminos.html')

def monalisa(request):
    context={}
    return render(request, 'aplicacion/monalisa.html')

def demoiselles(request):
    context={}
    return render(request, 'aplicacion/demoiselles.html')

def perfil(request):
    context={}
    return render(request, 'aplicacion/perfil.html')

def clocks(request):
    context={}
    return render(request, 'aplicacion/clocks.html')

def login(request):
    context={}
    return render(request, 'aplicacion/login.html')

def es_admin(user):
    return user.is_superuser

def acceso_denegado(request):
    return render(request, 'aplicacion/acceso_denegado.html')

@user_passes_test(es_admin, login_url='/acceso_denegado')
def crud(request):
    clientes = Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, 'aplicacion/crud.html', context)

def cliente_del(request,pk): ## DELETEADO DE CLIENTES
    context={}
    try:
        cliente=Cliente.objects.get(rut=pk)

        cliente.delete()
        mensaje="datos eliminados"
        cliente=Cliente.objects.all()
        context={'clientes': cliente,'mensaje':mensaje}
        return render(request, 'aplicacion/crud.html', context)
    except:
        mensaje="error, rut no existe"
        cliente=Cliente.objects.all()
        context={'clientes': cliente,'mensaje':mensaje}
        return render(request, 'aplicacion/crud.html', context)
    
def cliente_findEdit(request,pk): ## EDITOR DE CLIENTES
    if pk != "":
        cliente=Cliente.objects.get(rut=pk)
        ciudades=Ciudad.objects.all()

        print(type(cliente.id_ciudad.ciudad))

        context={'cliente':cliente,'ciudades':ciudades} ## ERA CIUDADES, NO CIUDAD
        if cliente:
            return render(request,'aplicacion/editar.html', context)
        else:
            context={'mensaje':"error, rut no existe"}
            return render(request, 'aplicacion/crud.html', context)

def editar(request):
    context={}
    return render(request, 'aplicacion/editar.html')

def cliente_add(request):
    if request.method == "POST":
        rut = request.POST.get("rut", "").strip()
        nombre = request.POST.get("nombre", "").strip()
        email = request.POST.get("email", "").strip()
        ciudad_id = request.POST.get("ciudad", "").strip()
        telefono = request.POST.get("telefono", "").strip()
        contrasena = request.POST.get("contrasena", "").strip()

        # Validaciones
        if not all([rut, nombre, email, ciudad_id, telefono, contrasena]):
            context = {
                'mensaje': "Debe rellenar todos los campos !!",
                'rut_value': rut,
                'nombre_value': nombre,
                'email_value': email,
                'telefono_value': telefono,
                'contrasena_value': contrasena,
            }
            return render(request, 'aplicacion/cliente_add.html', context)

        if not (telefono.isdigit() and len(telefono) == 9):
            context = {
                'mensaje': "Teléfono debe seguir el formato 9 y luego ocho dígitos.",
                'rut_value': rut,
                'nombre_value': nombre,
                'email_value': email,
                'contrasena_value': contrasena,
            }
            return render(request, 'aplicacion/cliente_add.html', context)

        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.fullmatch(regex, email):
            context = {
                'mensaje': "Email incorrecto !!",
                'rut_value': rut,
                'nombre_value': nombre,
                'telefono_value': telefono,
                'contrasena_value': contrasena,
            }
            return render(request, 'aplicacion/cliente_add.html', context)

        try:
            objCiudad = Ciudad.objects.get(id_ciudad=ciudad_id)
        except Ciudad.DoesNotExist:
            context = {
                'mensaje': "Ciudad no válida !!",
                'rut_value': rut,
                'nombre_value': nombre,
                'email_value': email,
                'telefono_value': telefono,
                'contrasena_value': contrasena,
            }
            return render(request, 'aplicacion/cliente_add.html', context)

        if Cliente.objects.filter(rut=rut).exists():
            context = {
                'mensaje': "RUT YA EXISTENTE !!",
                'nombre_value': nombre,
                'email_value': email,
                'telefono_value': telefono,
                'contrasena_value': contrasena,
            }
            return render(request, 'aplicacion/cliente_add.html', context)

        try:
            Cliente.objects.create(
                rut=rut,
                nombre=nombre,
                email=email,
                id_ciudad=objCiudad,
                telefono=telefono,
                contrasena=contrasena
            )
            context = {
                'mensaje': "Cliente añadido exitosamente !!"
            }
            return render(request, 'aplicacion/cliente_add.html', context)
        except IntegrityError:
            context = {
                'mensaje': "Error al añadir cliente. Verifique que los datos sean correctos.",
                'rut_value': rut,
                'nombre_value': nombre,
                'email_value': email,
                'telefono_value': telefono,
                'contrasena_value': contrasena,
            }
            return render(request, 'aplicacion/cliente_add.html', context)

    else:
        ciudades = Ciudad.objects.all()
        context = {'ciudades': ciudades}
        return render(request, 'aplicacion/cliente_add.html', context)


def perfil_vista(request):
    if 'cliente_id' not in request.session:
        return redirect('login')

    cliente_id = request.session.get('cliente_id')
    try:
        cliente = Cliente.objects.get(rut=cliente_id)
    except Cliente.DoesNotExist:
        return redirect('login')

    return render(request, 'aplicacion/perfil.html', {'cliente': cliente})


def logeo(request):
    print("1")
    
    if request.method == 'POST':
        print("2")
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        print(email + contrasena)
            
        try:
            print("3")
            cliente_ = Cliente.objects.get(email=email, contrasena=contrasena)
            print(cliente_)
            request.session['cliente_id'] = cliente_.rut
            print("xxx")
            return redirect('perfil') 
         
            
        except Cliente.DoesNotExist:
            print("4")
            mensaje = "Correo electrónico o contraseña incorrectos."
            return render(request, 'aplicacion/index.html', {'mensaje': mensaje})        
    return render(request, 'aplicacion/index.html')

def logout(request):
    try:
        del request.session['cliente_id']
    except KeyError:
        pass
    return redirect('index')


def cliente_update(request):
    if request.method == "POST":
        try:
            rut = request.POST.get("rut")
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            telefono = request.POST.get("telefono")
            ciudad_id = request.POST.get("ciudad")

            # Validar que todos los campos requeridos están presentes
            if not rut or not nombre or not email or not telefono or not ciudad_id:
                raise ValueError("Faltan datos requeridos")

            # Obtener el objeto Ciudad correspondiente al ID
            objCiudad = Ciudad.objects.get(id_ciudad=ciudad_id)

            # Crear o actualizar el cliente
            cliente, created = Cliente.objects.update_or_create(
                rut=rut,
                defaults={
                    'nombre': nombre,
                    'email': email,
                    'telefono': telefono,
                    'id_ciudad': objCiudad,
                }
            )

            # Mensaje de éxito y redirección
            messages.success(request, 'Los datos se actualizaron correctamente.')
            return redirect('editar_cliente')  # Ajusta el nombre de la vista según corresponda

        except Ciudad.DoesNotExist:
            messages.error(request, 'La ciudad seleccionada no existe.')
        except ValueError as ve:
            messages.error(request, str(ve))
        except Exception as e:
            messages.error(request, f'Error al actualizar los datos: {str(e)}')

    # Si no es un POST, o si hubo algún error, renderizar el formulario de edición
    ciudades = Ciudad.objects.all()
    context = {'ciudades': ciudades}
    return render(request, 'aplicacion/editar.html', context)
    
@user_passes_test(es_admin, login_url='/acceso_denegado')
def crud_ciudades(request):

    ciudades=Ciudad.objects.all()
    context={'ciudades':ciudades}
    print("Enviando datos... ")
    return render(request,"aplicacion/crud_ciudades.html",context)

@user_passes_test(es_admin, login_url='/acceso_denegado')
def ciudades_add(request):

    context={}

    if request.method == "POST":
        form = CiudadForm(request.POST)
        if form.is_valid:
            print("Formulario correcto")
            form.save()

            form=CiudadForm()

            context={'mensaje':"Datos grabados.","form":form}
            return render(request,'aplicacion/ciudades_add.html',context)
    else:
        form = CiudadForm()
        context={'form':form}
        return render(request,'aplicacion/ciudades_add.html',context)

def ciudades_del(request,pk):
    mensajes = []
    errores = []
    ciudades=Ciudad.objects.all()
    try:
        ciudad=Ciudad.objects.get(id_ciudad=pk)
        context={}
        if ciudad:
            ciudad.delete()
            mensajes.append["Ciudad eliminada."]
            context={'ciudades':ciudades,'mensajes':mensajes,'errores':errores}
            return render(request,'aplicacion/crud_ciudades.html',context)
    except:
        print("Error, id no existente")
        ciudades=Ciudad.objects.all()
        mensaje = "ID NO EXISTENTE"
        context = {'mensaje':mensaje,'ciudades':ciudades}
        return render(request,'aplicacion/crud_ciudades.html',context)

def ciudades_edit(request,pk):
    try:
        ciudad=Ciudad.objects.get(id_ciudad=pk)
        context={}
        if ciudad:
            print("Se encontró la ciudad.")
            if request.method == "POST":
                form = CiudadForm(request.POST,instance=ciudad)
                form.save()
                mensaje="Datos actualizados."
                print(mensaje)
                context={'ciudad': ciudad,'form': form, 'mensaje': mensaje}
                return render(request,'aplicacion/ciudades_edit.html',context)
            else:
                form=CiudadForm(instance=ciudad) ############ PODRÍA SERVER PARA EL RUT
                mensaje=""
                context={'ciudad': ciudad,'form': form, 'mensaje': mensaje}
                return render(request,'aplicacion/ciudades_edit.html',context)
    except:
        ciudades=Ciudad.objects.all()
        mensaje="ID NO EXISTENTE"
        context={'mensaje':mensaje,'ciudades':ciudades}
        return render(request,'aplicacion/ciudades_edit.html',context)

@login_required
def admin_site(request):
    request.session["usuario"]="iinocencio"
    usuario=request.session["usuario"]
    context={'usuario': usuario}
    return render(request,'registration/admin_site.html',context)

