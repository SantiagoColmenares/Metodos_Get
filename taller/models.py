from django.db import models


#Modelo jugador
class Jugador(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  dorsal = models.CharField(max_length=3)
  posicion = models.CharField(max_length = 20)
  estatura = models.CharField(max_length=20)


class Equipo(models.Model):
  nombre = models.CharField(max_length = 50)
  estadio = models.CharField(max_length=30)
  jugador = models.OneToOneField(Jugador, on_delete= models.CASCADE, null= False)







# Create your models here.
