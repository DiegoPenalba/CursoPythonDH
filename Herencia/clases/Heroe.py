from clases.Personaje import Personaje

class Heroe(Personaje):
    def __init__(self, nombre, salud, poder):
        super().__init__(nombre, salud) # Esto permite asignar los atributos heredados
        self.poder = poder
    
    def mostrarPoder(self):
        print(f"{self.nombre} tiene el poder de {self.poder}")