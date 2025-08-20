from clases.Heroe import Heroe
from clases.Villano import Villano

# Instancias
superman = Heroe("Superman", 1000, "Volar")
jocker = Villano("Jocker", 100, "Robar bancos")

# Programa

print("----------Metodos Heredados de Personaje----------")
superman.identificarse()
superman.mostrarSalud()
jocker.identificarse()
jocker.mostrarSalud()

print("----------Comportamientos propio de la clase----------")

superman.mostrarPoder()
jocker.mostrarHabilidad()
