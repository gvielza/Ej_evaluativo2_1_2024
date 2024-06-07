import sqlite3

#'''Realizar un sistema para gestionar la información de un Cine
#-Pelicula (titulo, duracion, genero) 
#-PeliculaAnimada (titulo, duracion, genero, estudio_animacion)
#-Cine (nombre, direccion) y una lista programación con las películas que se le irán agregando
#Implementar método mostrar_info() que muestra información específica de la película. La información de las películas se almacena en una base de datos SQLite, y el cine administra su programación.
#Poder gestionar las peliculas de la programación(CRUD)
#'''
import sqlite3

class Conexion:
    def __init__(self, nombre_bd):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()

    #Metodos para crear tablas

    def crear_tabla_peliculas(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pelicula (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(255) NOT NULL, duracion INT NOT NULL, genero VARCHAR(100) NOT NULL, UNIQUE(titulo, duracion, genero))")
        self.conexion.commit()

    def crear_tabla_peliculas_animadas(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS peliculaAnimada (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, duracion INTEGER NOT NULL, genero TEXT NOT NULL, estudio_animacion TEXT NOT NULL, UNIQUE(titulo, duracion, genero, estudio_animacion))")
        self.conexion.commit()

    def crear_tabla_cine(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cine (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, direccion TEXT NOT NULL, UNIQUE(nombre, direccion))")
        self.conexion.commit()

    def crear_tabla_programacion_peliculas(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS programacion_peliculas (id INTEGER PRIMARY KEY AUTOINCREMENT, cine_id INTEGER NOT NULL, pelicula_id INTEGER NOT NULL, fecha_hora TEXT NOT NULL, UNIQUE(cine_id, pelicula_id, fecha_hora), FOREIGN KEY (cine_id) REFERENCES cine(id), FOREIGN KEY (pelicula_id) REFERENCES pelicula(id))")
        self.conexion.commit()

    #Metodos para agregar

    def agregar_pelicula(self, titulo, duracion, genero):
        try:
            self.cursor.execute("INSERT INTO pelicula (titulo, duracion, genero) VALUES (?, ?, ?)", (titulo, duracion, genero))
            self.conexion.commit()
            print(f"La película '{titulo}' ha sido agregada a la base de datos.")
        except sqlite3.IntegrityError:
            print(f"La película '{titulo}' ya existe en la base de datos.")

    def agregar_pelicula_animada(self, titulo, duracion, genero, estudio_animacion):
        try:
            self.cursor.execute("INSERT INTO peliculaAnimada (titulo, duracion, genero, estudio_animacion) VALUES (?, ?, ?, ?)", (titulo, duracion, genero, estudio_animacion))
            self.conexion.commit()
            print(f"La película animada '{titulo}' ha sido agregada a la base de datos.")
        except sqlite3.IntegrityError:
            print(f"La película animada '{titulo}' ya existe en la base de datos.")

    def agregar_cine(self, nombre, direccion):
        try:
            self.cursor.execute("INSERT INTO cine (nombre, direccion) VALUES (?, ?)", (nombre, direccion))
            self.conexion.commit()
            print(f"El cine '{nombre}' ha sido agregado a la base de datos.")
        except sqlite3.IntegrityError:
            print(f"El cine '{nombre}' ya existe en la base de datos.")

    def agregar_programacion_pelicula(self, cine_id, pelicula_id, fecha_hora):
        self.cursor.execute("SELECT COUNT(*) FROM programacion_peliculas WHERE cine_id = ? AND pelicula_id = ? AND fecha_hora = ?", (cine_id, pelicula_id, fecha_hora))
        existe_programacion = self.cursor.fetchone()[0]
        if existe_programacion:
            print("La programación ya existe en la base de datos.")
        else:
            self.cursor.execute("INSERT INTO programacion_peliculas (cine_id, pelicula_id, fecha_hora) VALUES (?, ?, ?)", (cine_id, pelicula_id, fecha_hora))
            self.conexion.commit()
            print("Programación agregada correctamente.")

    #Metodos para actualizar

    def actualizar_pelicula(self, id, titulo, duracion, genero):
        self.cursor.execute("UPDATE pelicula SET titulo = ?, duracion = ?, genero = ? WHERE id = ?", (titulo, duracion, genero, id))
        self.conexion.commit()

    def actualizar_pelicula_animada(self, id, titulo, duracion, genero, estudio_animacion):
        self.cursor.execute("UPDATE peliculaAnimada SET titulo = ?, duracion = ?, genero = ?, estudio_animacion = ? WHERE id = ?", (titulo, duracion, genero, estudio_animacion, id))
        self.conexion.commit()

    def actualizar_cine(self, id, nombre, direccion):
        self.cursor.execute("UPDATE cine SET nombre = ?, direccion = ? WHERE id = ?", (nombre, direccion, id))
        self.conexion.commit()

    def actualizar_programacion_pelicula(self, id, cine_id, pelicula_id, fecha_hora):
        self.cursor.execute("UPDATE programacion_peliculas SET cine_id = ?, pelicula_id = ?, fecha_hora = ? WHERE id = ?", (cine_id, pelicula_id, fecha_hora, id))
        self.conexion.commit()

     #Metodos para mostrar

    def mostrar_peliculas(self):
        self.cursor.execute("SELECT * FROM pelicula")
        peliculas=self.cursor.fetchall()
        for pelicula in peliculas:
            print(pelicula)

    def mostrar_peliculas_animadas(self):
        self.cursor.execute("SELECT * FROM PeliculaAnimada")
        peliculas=self.cursor.fetchall()
        for pelicula in peliculas:
            print(pelicula)

    def mostrar_cines(self):
        self.cursor.execute("SELECT * FROM Cine")
        cines=self.cursor.fetchall()
        for cine in cines:
            print(cine)

    def mostrar_programacion(self):
        self.cursor.execute("SELECT * FROM Programacion")
        programacion=self.cursor.fetchall()
        for programacion in programacion:
            print(programacion)

    def mostrar_programacion(self, cine_id):
        self.cursor.execute("""
            SELECT pelicula.titulo, programacion_peliculas.fecha_hora 
            FROM programacion_peliculas
            JOIN pelicula ON programacion_peliculas.pelicula_id = pelicula.id
            WHERE programacion_peliculas.cine_id = ?
        """, (cine_id,))
        programacion = self.cursor.fetchall()
        if not programacion:
            print("No hay películas programadas.")
        else:
            for titulo, fecha_hora in programacion:
                print(f"Película: {titulo}, Fecha y hora: {fecha_hora}")

     #Metodos para eliminar

    def eliminar_pelicula(self, id):
        self.cursor.execute("DELETE FROM pelicula WHERE id = ?", (id,))
        self.conexion.commit()

    def eliminar_pelicula_animada(self, id):
        self.cursor.execute("DELETE FROM peliculaAnimada WHERE id = ?", (id,))
        self.conexion.commit()

    def eliminar_cine(self, id):
        self.cursor.execute("DELETE FROM cine WHERE id = ?", (id,))
        self.conexion.commit()

    def eliminar_programacion_pelicula(self, id):
        self.cursor.execute("DELETE FROM programacion_peliculas WHERE id = ?", (id,))
        self.conexion.commit()

    #Metodo para cerrar la conexion

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
