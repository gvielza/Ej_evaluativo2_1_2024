#'''Realizar un sistema para gestionar la información de un Cine
#-Pelicula (titulo, duracion, genero) 
#-PeliculaAnimada (titulo, duracion, genero, estudio_animacion)
#-Cine (nombre, direccion) y una lista programación con las películas que se le irán agregando
#Implementar método mostrar_info() que muestra información específica de la película. La información de las películas se almacena en una base de datos SQLite, y el cine administra su programación.
#Poder gestionar las peliculas de la programación(CRUD)
#'''

from clases.pelicula import Pelicula

#Pruebo creando una pelicula 
pelicula=Pelicula("La La Land", 128,"Musical")
pelicula.mostrar_info()
