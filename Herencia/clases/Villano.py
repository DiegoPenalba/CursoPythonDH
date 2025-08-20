from clases.Personaje import Personaje

class Villano(Personaje):
    def __init__(self, nombre, salud, habilidad):
        super().__init__(nombre, salud) # Esto permite asignar los atributos heredados
        self.habilidad = habilidad
    
    def mostrarHabilidad(self):
        print(f"{self.nombre} tiene la habilidad de {self.habilidad}")