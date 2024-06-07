#'''Realizar un sistema para gestionar la información de un Cine
#-Pelicula (titulo, duracion, genero) 
#-PeliculaAnimada (titulo, duracion, genero, estudio_animacion)
#-Cine (nombre, direccion) y una lista programación con las películas que se le irán agregando
#Implementar método mostrar_info() que muestra información específica de la película. La información de las películas se almacena en una base de datos SQLite, y el cine administra su programación.
#Poder gestionar las peliculas de la programación(CRUD)
#'''

from clases.pelicula import Pelicula
from base_datos.conexion import Conexion
from clases.cine import Cine

# Conexión a la base de datos
conexion = Conexion("base_datos/cine.db")
print("Conectado a la base de datos")

# Crear las tablas
conexion.crear_tabla_peliculas()
conexion.crear_tabla_peliculas_animadas()
conexion.crear_tabla_cine()
conexion.crear_tabla_programacion_peliculas()

# Crear cines
hoyts = Cine(1, "Hoyts", "Av. Corrientes 123")
cinemark = Cine(2, "Cinemark", "Av. Santa Fe 456")
print("Cines creados")

# Agregar cines a la base de datos
conexion.agregar_cine(hoyts.nombre, hoyts.direccion)
conexion.agregar_cine(cinemark.nombre, cinemark.direccion)

# Crear películas y agregarlas a la base de datos
pelicula1 = Pelicula("La La Land", 128, "Musical")
pelicula2 = Pelicula("Toy Story", 81, "Animación")
pelicula3 = Pelicula("Inception", 148, "Ciencia Ficción")
conexion.agregar_pelicula(pelicula1.get_titulo(), pelicula1.get_duracion(), pelicula1.get_genero())
conexion.agregar_pelicula(pelicula2.get_titulo(), pelicula2.get_duracion(), pelicula2.get_genero())
conexion.agregar_pelicula(pelicula3.get_titulo(), pelicula3.get_duracion(), pelicula3.get_genero())

# Agregar películas a la programación de los cines
conexion.agregar_programacion_pelicula(hoyts.id, 1, "2024-06-10 20:00")
conexion.agregar_programacion_pelicula(hoyts.id, 2, "2024-06-11 18:00")
conexion.agregar_programacion_pelicula(cinemark.id, 3, "2024-06-12 21:00")
conexion.agregar_programacion_pelicula(cinemark.id, 1, "2024-06-13 17:00")

# Mostrar programación de los cines
print("Programación del Cine Hoyts:")
conexion.mostrar_programacion(hoyts.id)

print("\nProgramación del Cine Cinemark:")
conexion.mostrar_programacion(cinemark.id)

# Eliminar una película de la programación y mostrar la programación actualizada
conexion.eliminar_programacion_pelicula(1)  # Suponiendo que la ID del registro en la tabla programacion_peliculas es 1
print("\nProgramación actualizada del Cine Hoyts:")
conexion.mostrar_programacion(hoyts.id)
