class PeliculaAnimada:
    def __init__(self, id, titulo, duracion, genero, estudio_animacion):
        self.id = id
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.estudio_animacion = estudio_animacion

    def set_id(self, seteo_id):
        self.id = seteo_id
    
    def set_titulo(self, seteo_titulo):
        self.titulo = seteo_titulo
    
    def set_duracion(self, seteo_duracion):
        self.duracion = seteo_duracion

    def set_genero(self, seteo_genero):
        self.genero = seteo_genero
    def set_estudio_animacion(self, seteo_estudio_animacion):
        self.estudio_animacion = seteo_estudio_animacion
    
    def get_id(self):
        return self.id
    def get_titulo(self):
        return self.titulo
    def get_duracion(self):
        return self.duracion
    def get_genero(self):
        return self.genero
    def get_estudio_animacion(self):
        return self.estudio_animacion
    
    def mostrar_info(self):
        print("la pelicula se llama", self.titulo)
        print("la pelicula animada tiene una duracion de ",self.duracion, "minutos")
        print("la pelicula animada es del genero ", self.genero)
        print("la pelicula animada es de ", self.estudio_animacion)

        