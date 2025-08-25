import random


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 100
        self.nivel = 1
        self.experiencia = 0
    
    def atacar(self):
        return random.randint(10,20) * self.nivel
    
    def recibirDano(self, dano):
        self.salud -= dano
        if(self.salud) <= 0:
            print(f"El jugador: {self.nombre}, ha muerto")
        else:
            print(f"Te quedan {self.salud} puntos de salud")
    
    def ganarExperiencia(self, experiencia):
        print(f"El jugador: {self.nombre}, ha ganado {experiencia} puntos de experiencia")
        self.experiencia += experiencia
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"El jugador: {self.nombre}, ha subido al nivel {self.nivel}")
    

