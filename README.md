## Ejercicio #2
Realizar un sistema para gestionar la información de un Cine
-Pelicula (titulo, duracion, genero) 
-PeliculaAnimada (titulo, duracion, genero, estudio_animacion)
-Cine (nombre, direccion) y una lista programación con las películas que se le irán agregando
Implementar método mostrar_info() que muestra información específica de la película. La información de las películas se almacena en una base de datos SQLite, y el cine administra su programación.
Poder gestionar las peliculas de la programación(CRUD)

Mateo Canzani: Documentación del Ejercicio(Readme)

Tatiana: Implementación de la Clase Pelicula

Sarai: Implementación de la Clase PeliculaAnimada

Leandro Madrid: Implementación de la Clase Cine

Ezequiel Roel: Configuración y Manejo de la Base de Datos SQLite

Daniel Salerno:  Pruebas Unitarias


Descripción General:
Este sistema gestiona la información de un cine, incluyendo la administración de películas (regulares y animadas) y la programación de las mismas en diferentes cines.La información se almacena en una base de datos SQLite para asegurar la persistencia de los datos.

Requisitos:
Para ejecutar esta aplicación, se necesitan los siguientes requisitos:
Python 3.x
SQLite3

Cómo se Hizo:
El proyecto se  realizó mediante un repositorio en GitHub, en el cual los alumnos fueron subiendo el código.
La implementación del sistema se realizó utilizando clases en Python para representar películas, películas animadas y cines. Además, se utiliza SQLite para la persistencia de datos.

Clases:

Clase Conexion: Esta clase maneja la conexión a la base de datos SQLite y proporciona métodos para crear tablas, y realizar operaciones CRUD.

Clase Película: Representa una película con atributos de título, duración y género, e incluye un método para mostrar la información de la película.

Clase PeliculaAnimada: Hereda de Película y agrega un atributo adicional para el estudio de animación.

Clase Cine: Representa un cine con atributos de nombre y dirección, y maneja la programación de películas.
.
Clase Main: Este script principal integra todas las clases y métodos anteriores para interactuar con el sistema, demostrando su uso práctico.



Funcionalidades:
 Las funcionalidades principales incluyen la creación, lectura, actualización y eliminación (CRUD) de películas y cines así como la gestión de la programación de películas. 
.
Enlace al repositorio:  https://github.com/gvielza/Ej_evaluativo2_1_2024.git
