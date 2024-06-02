
class Pelicula():
    #constructor
    def __init__(self,titulo,duracion,genero):
        self.titulo=titulo
        self.duracion=duracion
        self.genero=genero

#getter y setters
    def set_titulo(self,seteo_titulo):
        self.titulo=seteo_titulo
    def set_duracion(self,seteo_duracion):
        self.duracion=seteo_duracion
    def set_genero(self,seteo_genero):
        self.genero=seteo_genero

    def get_titulo(self):
        return self.titulo
    def get_duracion(self):
        return self.duracion
    def get_genero(self):
        return self.genero

#Metodo de mostrar informacion de peliculas
    def mostrar_info(self):
        print("La pelicula se llama ", self.titulo)
        print("La pelicula tiene una duración de ", self.duracion,"minutos")
        print("La pelicula es del género ", self.genero)
