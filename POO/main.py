from clases.Perro import Perro

# Instantia la clase (objeto)
perro1 = Perro("Peppo", 4) # llama al constructor __init__ y crea un objeto perro1 de la clase Perro
perro2 = Perro("Luna", 5) # llama al constructor __init__ y crea un objeto perro2 de la clase Perro

# Imprime los atributos de los objetos
print(f"{perro1.nombre} tiene {perro1.edad} años y dice: {perro1.ladrar()}")
print(f"{perro2.nombre} tiene {perro2.edad} años y dice: {perro2.ladrar()}")