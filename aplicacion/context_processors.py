from .models import Cliente  

def custom_context(request):
    context = {}
    
    # Verificar si hay un cliente autenticado en la sesión
    if 'cliente_id' in request.session:
        cliente_id = request.session['cliente_id']
        try:
            cliente_obj = Cliente.objects.get(rut=cliente_id)
            context['is_authenticated'] = True
            context['cliente'] = cliente_obj
        except Cliente.DoesNotExist:
            context['is_authenticated'] = False
            context['cliente'] = None
    else:
        context['is_authenticated'] = False
        context['cliente'] = None
    
    mensaje = None
    if 'mensaje' in request.session:
        mensaje = request.session.pop('mensaje') 
    context['mensaje_modal'] = mensaje
    
    return context