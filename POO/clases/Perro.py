# Definiendo la clase (Plantilla)
class Perro:
    # Metodo constructor
    # Se ejecuta al crear un objeto de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributo de nombre de la instancia, le asignamos el valor del argumento en el constructor
        self.edad = edad # Atributo de edad de la instancia, le asignamos el valor del argumento en el constructor
        
    # Metodo para ladrar
    def ladrar(self):
        return "¡Guau!"
