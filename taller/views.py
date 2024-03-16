from django.shortcuts import render
from django.http import HttpResponse
from .models import Jugador, Equipo


def index(request):
  return render(request, "index.html", {})

def get_jugador(response,nombre, apellido, dorsal, posicion, estatura):
  jugador = Jugador(nombre   = nombre,
                    apellido = apellido,
                    dorsal   = dorsal,
                    posicion = posicion,
                    estatura = estatura
                    )
  jugador.save()
  return HttpResponse("Gracias 😸")

def get_equipo(response, nombre, estadio, jugador):
  # print(id)
  # print(Jugador.objects.get(id = 1))
  equipo = Equipo(nombre = nombre, estadio = estadio, id = jugador)
  # equipo = Equipo(nombre = nombre, estadio = estadio, jugador = id)
  
  equipo.save() 

  return HttpResponse("Gracias 👌")


