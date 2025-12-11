from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # Para facilitar el POST desde Vue
from .models import Cupon
import json

# 1. La vista que carga tu página web
def index(request):
    return render(request, 'index.html')

# Vista para la página de cupones (separada)
def cupones_view(request):
    return render(request, 'cupones.html')

# 2. La API que entrega los datos a Vue
def lista_cupones(request):
    # Traemos todos los activos. Ordenamos para que los canjeados se vayan al fondo si quieres.
    cupones = Cupon.objects.filter(activo=True).order_by('fue_canjeado', 'fecha_expiracion')
    
    data = []
    for c in cupones:
        data.append({
            'id': c.id,
            'titulo': c.titulo,
            'descripcion': c.descripcion,
            'codigo': c.codigo,
            'imagen': c.imagen.url if c.imagen else '', # La URL de la foto
            'fecha_expiracion': c.fecha_expiracion.strftime('%d/%m/%Y'),
            'fue_canjeado': c.fue_canjeado,
            'vencido': c.esta_vencido
        })
    return JsonResponse({'cupones': data})

# 3. La API para canjear (usamos csrf_exempt por simplicidad en este MVP)
@csrf_exempt
def canjear_cupon(request, id):
    if request.method == 'POST':
        cupon = get_object_or_404(Cupon, id=id)
        cupon.fue_canjeado = True
        cupon.save()
        return JsonResponse({'success': True, 'message': 'Cupón canjeado correctamente'})
    return JsonResponse({'success': False}, status=400)


import os
from django.conf import settings

def lista_fotos_cronologicas(request):
    path = os.path.join(settings.MEDIA_ROOT, 'fotos_cronologicas')
    fotos = []
    if os.path.exists(path):
        # Listamos los archivos y los ordenamos alfabéticamente (que ahora es cronológico)
        archivos = sorted([f for f in os.listdir(path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4'))])
        for f in archivos:
            fotos.append({
                'url': f'/media/fotos_cronologicas/{f}',
                'year': f.split('_')[0] # Extraemos el año del nombre (2021_...)
            })
    return JsonResponse({'fotos': fotos})