# ----------------------------
# DICCIONARIOS EN PYTHON
# ----------------------------

ejemploDiccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero",
    "tenologias": ["Python", "JavaScript", "C++"]
}

print("------------DICCIONARIOS EN PYTHON------------")

print(ejemploDiccionario)  # Imprime el diccionario completo
print(ejemploDiccionario["nombre"])  # Imprime el valor asociado a la clave "nombre"
print(ejemploDiccionario.get("edad"))  # Imprime el valor asociado a la clave "edad" (otra forma de acceder)
print(ejemploDiccionario["tenologias"])  # Imprime la lista de tecnologías
print(ejemploDiccionario["tenologias"][0])  # Imprime la primera tecnología en la lista

claves = ejemploDiccionario.keys()  # Obtiene todas las claves del diccionario
valores = ejemploDiccionario.values()  # Obtiene todos los valores del diccionario
items = ejemploDiccionario.items()  # Obtiene todos los pares clave-valor del diccionario

print(f"estas son las claves: {claves}")  # Imprime las claves
print(f"estas son los valores: {valores}")  # Imprime los valores
print(f"estas son los items: {items}")  # Imprime los pares clave-valor

ejemploDiccionario["edad"] = 31  # Actualiza el valor asociado a la clave "edad"
ejemploDiccionario["pais"] = "España"  # Añade una nueva clave "pais" con su valor
print(ejemploDiccionario)  # Imprime el diccionario modificado

ejemploDiccionario.pop("profesion")
ejemploDiccionario.popitem()  # Elimina el último par clave-valor añadido
print(ejemploDiccionario)  # Imprime el diccionario después de eliminar un elemento

print("------------Recorrer un Diccionario------------")
# Bucle for para recorrer un diccionario
for clave in ejemploDiccionario:  # Recorre las claves del diccionario
    print(f"{clave}: {ejemploDiccionario[clave]}")  # Imprime cada clave y su valor asociado    

for clave, valor in ejemploDiccionario.items():  # Recorre los pares clave-valor
    print(f"{clave}: {valor}")

print("------------Diccionarios anidados------------")
# Diccionario anidado (diccionario dentro de otro diccionario)
familia = {
    "mama": {
        "nombre": "Ana",
        "edad": 25
    },
    "papa": {
        "nombre": "Luis",
        "edad": 28
    },
    "hijos": {
        "nombre": "Carlos",
        "edad": 5
    }
}

print(familia)  # Imprime el diccionario anidado completo
print(familia["mama"]["nombre"])  # Imprime el nombre de la persona1
print(familia["papa"]["edad"])  # Imprime la edad de la persona2

padre = {
    "nombre": "Luis",
    "edad": 28
}

madre = {
    "nombre": "Ana",
    "edad": 25
}

hijo = {
    "nombre": "Carlos",
    "edad": 5
}

familia2 = {
"Papa": padre,
"Mama": madre,
"Querubin": hijo
}

print(familia2)

for miembro, datos in familia2.items():  # Recorre los miembros de la familia
    print(f"{miembro}: {datos['nombre']} tiene {datos['edad']} años")  # Imprime el nombre y la edad de cada miembro
    # Accede a los datos de cada miembro usando su clave
    for clave in datos:  # Recorre las claves de cada miembro
        print(f"{clave}: {datos[clave]}")