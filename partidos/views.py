from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Partido
from .forms import PartidoForm
from datetime import datetime

def index(request):
    partidos = Partido.objects.all().order_by('-fecha')
    return render(request, 'partidos/index.html', {'partidos': partidos})

def agregar_partido(request):
    if request.method == 'POST':
        # Crear partido MANUALMENTE con formato de fecha corregido
        try:
            # Convertir la fecha del formato datetime-local a formato Django
            fecha_str = request.POST.get('fecha')
            fecha_formateada = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
            
            Partido.objects.create(
                equipo_local=request.POST.get('equipo_local'),
                equipo_visitante=request.POST.get('equipo_visitante'),
                fecha=fecha_formateada,
                estadio=request.POST.get('estadio'),
                goles_local=int(request.POST.get('goles_local', 0)),
                goles_visitante=int(request.POST.get('goles_visitante', 0))
            )
            # Redirigir inmediatamente a la lista
            return redirect('index')
        except Exception as e:
            # Si hay error, mostrar mensaje
            return render(request, 'partidos/agregar_partido.html', {'error': str(e)})
    
    # Si es GET, mostrar formulario vacío
    return render(request, 'partidos/agregar_partido.html')

def editar_partido(request, id_partido):
    partido = get_object_or_404(Partido, pk=id_partido)
    if request.method == 'POST':
        # Actualizar partido manualmente
        try:
            # Convertir la fecha del formato datetime-local a formato Django
            fecha_str = request.POST.get('fecha')
            fecha_formateada = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
            
            partido.equipo_local = request.POST.get('equipo_local')
            partido.equipo_visitante = request.POST.get('equipo_visitante')
            partido.fecha = fecha_formateada
            partido.estadio = request.POST.get('estadio')
            partido.goles_local = int(request.POST.get('goles_local', 0))
            partido.goles_visitante = int(request.POST.get('goles_visitante', 0))
            partido.save()
            return redirect('index')
        except Exception as e:
            return render(request, 'partidos/editar_partido.html', {'partido': partido, 'error': str(e)})
    
    # Si es GET, mostrar formulario con datos actuales
    return render(request, 'partidos/editar_partido.html', {'partido': partido})

def eliminar_partido(request, id_partido):
    partido = get_object_or_404(Partido, pk=id_partido)
    if request.method == 'POST':
        partido.delete()
        return redirect('index')
    return render(request, 'partidos/eliminar_partido.html', {'partido': partido})