# ----------------------------
# TUPLAS EN PYTHON
# ----------------------------

tuplasFrutas = ("Manzana", "Uva", "Fresa", "Mandarina", "Aguacate", "Naranja", "Kiwi")

print("------------TUPLAS EN PYTHON------------")

print(tuplasFrutas)  # Imprime la tupla completa
print(tuplasFrutas[0])  # Imprime el primer elemento de la tupla.
print(tuplasFrutas[-1])  # Imprime el último elemento de la tupla.
print(tuplasFrutas[1:4])  # Imprime los elementos desde el índice 1 hasta el 3 (excluyendo el 4).
print(tuplasFrutas[2:])  # Imprime los elementos desde el índice 2 hasta el final de la tupla.
print(tuplasFrutas[:3])  # Imprime los primeros tres elementos de la tupla.
if "Fresa" in tuplasFrutas:  # Comprueba si "Fresa" está en la tupla. (palabra clave in)
    print("Fresa está en la tupla")


print("------------Actualizacion de Tuplas------------")

listaDesdeTupla = list(tuplasFrutas)  # Convierte la tupla en una lista
listaDesdeTupla[1] = "Pera"  # Cambia el elemento en el índice 1 a "Pera"
tuplasFrutas = tuple(listaDesdeTupla)  # Convierte la lista de nuevo en una tupla
print(tuplasFrutas)  # Imprime la tupla modificada
# se puede hacer .append, .insert, .remove, .pop, del, clear, extend, count, index
# pero solo despues de convertir la tupla en una lista

# lo que si se puede hacer es concatenar tuplas
nuevaTupla = tuplasFrutas + ("Cereza", "Melon")  # Crea una nueva tupla concatenando dos tuplas
print(nuevaTupla)  # Imprime la nueva tupla

print("------------Desempaqutando Tuplas------------")
# Desempaquetado de tuplas (asignar valores de la tupla a variables individuales)

(a, b, c, d, e, f, g) = tuplasFrutas  # Asigna cada elemento de la tupla a una variable

print(a)  # Imprime el valor de la variable a (Manzana)
print(b)  # Imprime el valor de la variable b (Pera)
print(c)  # Imprime el valor de la variable c (Fresa)
print(d)  # Imprime el valor de la variable d (Mandarina)
print(e)  # Imprime el valor de la variable e (Aguacate)
print(f)  # Imprime el valor de la variable f (Naranja)
print(g)  # Imprime el valor de la variable g (Kiwi)

# Si la tupla tiene más elementos que variables, se puede usar el operador * para capturar los elementos restantes. (los elementos no asignados)
(x, y, *z) = tuplasFrutas  # Asigna los dos primeros elementos a x e y, y el resto a z como una lista

print(x)  # Imprime el valor de la variable x (Manzana)
print(y)  # Imprime el valor de la variable y (Pera)
print(z)  # Imprime la lista z con los elementos restantes ['Fresa', 'Mandarina', 'Aguacate', 'Naranja', 'Kiwi']

print("------------Bucle en Tuplas------------")
# Bucle for para recorrer una tupla
for i in range(len(tuplasFrutas)):  # Recorre la tupla usando un índice
    print(tuplasFrutas[i], f"con su indice: {i}", )  # Imprime cada fruta usando su índice

print("------------Bucle While en Tuplas------------")

while i < len(tuplasFrutas):  # Mientras el índice sea menor que la longitud de la tupla
    print(tuplasFrutas[i])
    print(i)
    i += 1  # Incrementa el índice en 1

print("------------Juntar, contar y ver Tuplas------------")

tuplasFrutas1 = ("Manzana", "Uva", "Fresa")
tuplasFrutas2 = ("Mandarina", "Aguacate", "Naranja")

tuplasJuntas = tuplasFrutas1*2 + tuplasFrutas2  # Une dos tuplas en una nueva tupla
print(tuplasJuntas)  # Imprime la tupla unida

print(tuplasJuntas.count("Manzana"))  # Cuenta cuántas veces aparece "Manzana" en la tupla
print(tuplasJuntas.index("Fresa"))  # Devuelve el índice de la primera aparición de "Fresa"

print("------------Comprensiones de Tuplas------------")