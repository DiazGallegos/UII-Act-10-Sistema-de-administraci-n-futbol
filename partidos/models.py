from django.db import models

class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    equipo_local = models.CharField(max_length=100)
    equipo_visitante = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    estadio = models.CharField(max_length=100)
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"