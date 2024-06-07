class PeliculaAnimada:
    def __init__(self, titulo, duracion, genero, estudio_animacion):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.estudio_animacion = estudio_animacion

    def mostrar_info(self):
        return f"Titulo: {self.titulo}\nDuración: {self.duracion} minutos\nGénero: {self.genero}\nEstudio de Animación: {self.estudio_animacion}"