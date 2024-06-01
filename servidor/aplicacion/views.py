from django.shortcuts import render

# Create your views here.

def base(request):
    context={}
    return render(request, 'aplicacion/base.html')

def index(request):
    context={}
    return render(request, 'aplicacion/index.html', context)

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