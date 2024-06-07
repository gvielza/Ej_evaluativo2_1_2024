# Clase Cine
class Cine:
    # Constructor
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.programacion = []

    # Agregar a programación
    def agregar_a_programacion(self, pelicula, fecha_hora):
        self.programacion.append((pelicula, fecha_hora))

    # Eliminar de programación
    def eliminar_de_programacion(self, pelicula):
        self.programacion = [p for p in self.programacion if p[0] != pelicula]

    # Mostrar programación
    def mostrar_programacion(self):
        if not self.programacion:
            print("No hay películas programadas.")
        else:
            print(f"Programación de {self.nombre}:")
            for pelicula, fecha_hora in self.programacion:
                print(f"Fecha y hora: {fecha_hora}")
                pelicula.mostrar_info()

    # Mostrar Info
    def mostrar_info(self):
        print(f"Cine: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        self.mostrar_programacion()
        