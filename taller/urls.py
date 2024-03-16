from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('jugador/<str:nombre>/<str:apellido>/<int:dorsal>/<str:posicion>/<int:estatura>', views.get_jugador, name="jugador"),
    path('equipo/<str:nombre>/<str:estadio>/<int:jugador>', views.get_equipo, name="equipo")
]