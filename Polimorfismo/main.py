# from clases.Animal import Animal
from clases.Perro import Perro
from clases.Gato import Gato
from clases.Vaca import Vaca

def hacerSonidoDeAnimal(animal):
    print(f"{animal.nombre} hace {animal.hacerSonido()}")

perro = Perro("Peppo")
gato = Gato("Pelusa")
vaca = Vaca("Lechera")

hacerSonidoDeAnimal(perro)
hacerSonidoDeAnimal(gato)
hacerSonidoDeAnimal(vaca)