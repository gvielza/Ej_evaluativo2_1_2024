#'''Realizar un sistema para gestionar la información de un Cine
#-Pelicula (titulo, duracion, genero) 
#-PeliculaAnimada (titulo, duracion, genero, estudio_animacion)
#-Cine (nombre, direccion) y una lista programación con las películas que se le irán agregando
#Implementar método mostrar_info() que muestra información específica de la película. La información de las películas se almacena en una base de datos SQLite, y el cine administra su programación.
#Poder gestionar las peliculas de la programación(CRUD)
#'''

from clases.pelicula import Pelicula
from base_datos.conexion import Conexion

#Conexion a base de datos
conexion = Conexion("base_datos/cine.db")
print("Conectado a la base de datos")

#Se crean las tablas
conexion.crear_tabla_peliculas()
conexion.crear_tabla_peliculas_animadas()
conexion.crear_tabla_cine()
conexion.crear_tabla_programacion_peliculas()

#Se crea cine (A modo de ejemplo)
conexion.agregar_cine(1, "Hoyts", "Av. Corrientes 123")

#Pruebo creando una pelicula 
pelicula = Pelicula("La La Land", 128, "Musical")
conexion.agregar_pelicula(1, pelicula.get_titulo(), pelicula.get_duracion(), pelicula.get_genero())
conexion.agregar_programacion_pelicula(1, 1, 1, "2021-10-10 20:00")
pelicula.mostrar_info()
