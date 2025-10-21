from django.contrib import admin
from .models import Partido

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('equipo_local', 'equipo_visitante', 'fecha', 'estadio', 'goles_local', 'goles_visitante')
    list_filter = ('fecha', 'estadio')
    search_fields = ('equipo_local', 'equipo_visitante', 'estadio')