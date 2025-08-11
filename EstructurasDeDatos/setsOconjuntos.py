# ----------------------------
# SETS EN PYTHON
# ----------------------------

conjuntosFrutas = {"Manzana", "Uva", "Fresa"}
conjuntoFrutasTropicales = {"Piña", "Coco", "Mango"}

print("------------SETS EN PYTHON------------")

print(conjuntosFrutas)  # Imprime el conjunto completo
print("Manzana" in conjuntosFrutas)  # Comprueba si "Manzana" está en el conjunto
conjuntosFrutas.add("Kiwi")  # Añade "Kiwi" al conjunto
conjuntosFrutas.pop()  # Elimina y devuelve un elemento aleatorio del conjunto
conjuntosFrutas.update(conjuntoFrutasTropicales) 

print(conjuntosFrutas) # Añade todos los elementos de conjuntoFrutasTropicales al conjunto

conjuntosFrutas.remove("Uva")  # Elimina "Uva" del conjunto (lanza error si no existe)
conjuntosFrutas.discard("Fresa")  # Elimina "Fresa" del conjunto (no lanza error si no existe)

print(conjuntosFrutas)  # Imprime el conjunto modificado

print("------------Operaciones de Conjuntos------------")

conjuntoLetras = {"a", "b", "c", "d", 1}
conjuntoNumeros = {1, 2, 3, 4}

# Union: Combina todos los elementos de ambos conjuntos, eliminando duplicados.
union = conjuntoLetras.union(conjuntoNumeros)
print("Union:", union)
union2 = conjuntoLetras | conjuntoNumeros  # Operador |
print("Union con operador | :", union2)

# Intersección: Obtiene los elementos comunes entre ambos conjuntos.
interseccion = conjuntoLetras.intersection(conjuntoNumeros)
print("Intersección:", interseccion)
interseccion2 = conjuntoLetras & conjuntoNumeros  # Operador &
print("Intersección con operador & :", interseccion2)

# Diferencia: Obtiene los elementos que están en el primer conjunto pero no en el segundo.
diferencia = conjuntoLetras.difference(conjuntoNumeros)
print("Diferencia:", diferencia)
diferencia2 = conjuntoLetras - conjuntoNumeros  # Operador -
print("Diferencia con operador - :", diferencia2)