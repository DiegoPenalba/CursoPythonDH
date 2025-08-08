# ----------------------------
# LISTAS EN PYTHON
# ----------------------------
print("------------LISTAS EN PYTHON------------")

listaEjemplo = ["Manzana", "Pera", "Uva", "Fresa", "Manzana", "Mandarina"]
lista1 = ["Manzana", "Pera", "Uva"]
frutas = ["Fresa", "Manzana", "Mandarina"]
tuplaEjemplo = ("Manzana", "Pera", "Uva")

print(listaEjemplo)  # Imprime la lista completa
print(listaEjemplo[0])  # Imprime el primer elemento de la lista.
print(listaEjemplo[-1])  # Imprime el último elemento de la lista.
print(listaEjemplo[1:4])  # Imprime los elementos desde el índice 1 hasta el 3 (excluyendo el 4).
print(listaEjemplo[2:])  # Imprime los elementos desde el índice 2 hasta el final de la lista.
print(listaEjemplo[:3])  # Imprime los primeros tres elementos de la lista.
if "Pera" in listaEjemplo:  # Comprueba si "Pera" está en la lista. (palabra clave in)
    print("Pera está en la lista")
listaEjemplo[3] = "Frutilla"  # Cambia el elemento en el índice 3 a "Frutilla"
listaEjemplo.insert(2, "Aguacate")  # Inserta "Aguacate" en el índice 2 el resto de la lista se desplaza
listaEjemplo.append("Kiwi")  # Añade "Kiwi" al final de la lista
lista1.extend(frutas)  # Añade todos los elementos de frutas al final de lista1
frutas.extend(tuplaEjemplo)  # Añade todos los elementos de tuplaEjemplo al final de frutas
listaEjemplo.remove("Manzana")  # Elimina la primera aparición de "Manzana" de la lista
listaEjemplo.pop(2)  # Elimina el elemento en el índice 2 y lo devuelve
listaEjemplo.pop()  # Elimina y devuelve el último elemento de la lista
del listaEjemplo[3] # Elimina el elemento en el índice 3 sin devolverlo
lista1.clear()  # Elimina todos los elementos de lista1
print(listaEjemplo.count("Manzana"))  # Cuenta cuántas veces aparece "Manzana" en la lista
print(listaEjemplo.index("Frutilla"))  # Devuelve el índice de la primera aparición de "Fresa"

# ----------------------------
# BUCLES EN LISTAS
# ----------------------------
print("------------BUCLES EN LISTAS------------")

# Bucle for para recorrer una lista
for fruta in frutas:  # Recorre cada elemento de la lista
    print(fruta)  # Imprime cada fruta en la lista

# Bucle for con indice disponible
print(len(frutas))  # Imprime la longitud de la lista frutas
for i in range(len(frutas)):  # Recorre la lista usando un índice
    print(frutas[i])  # Imprime cada fruta usando su índice
    print(i)

# Bucle while para recorrer una lista con un índice
i = 0  # Inicializa el índice en 0
while i < len(frutas):  # Mientras el índice sea menor que la longitud de la lista
    print(frutas[i])  # Imprime la fruta en el índice actual
    i += 1  # Incrementa el índice en 1

# shorthand para recorrer una lista
[print(fruta) for fruta in frutas]  # Imprime cada fruta en la lista usando una comprensión de lista

# ----------------------------
# COMPRENSIONES DE LISTAS: Tecnicas de Sintax para crear listas de manera concisa. Abreviaciones
# ----------------------------
print("------------COMPRENSIONES DE LISTAS------------")

frutasConE = []
for fruta in frutas:  # Recorre cada fruta en la lista
    if "e" in fruta:  # Comprueba si la letra "e" está en la fruta
        frutasConE.append(fruta)  # Añade la fruta a la nueva lista si contiene "e" 
frutasConE = [fruta for fruta in frutas if "e" in fruta]  # Comprensión de lista para crear una nueva lista con frutas que contienen "e"
frutasSinMandarina = [fruta for fruta in frutas if "Mandarina" != fruta]  # Crea una nueva lista sin "Mandarina"
listaDeRangos = [x for x in range(10)]  # Crea una lista de números del 0 al 9
listaDeRangos2 = [x for x in range(10) if x % 2 == 0]  # Crea una lista de números pares del 0 al 9
mayusculas = [fruta.upper() for fruta in frutas]  # Crea una lista de frutas en mayúsculas  
frutas2 = [ fruta if fruta != "Pera" else "Aguacate" for fruta in frutas]
print(frutas2)  # Imprime la nueva lista donde "Pera" ha sido reemplazada por "Aguacate"
# Crea una nueva lista reemplazando "Pera" por "Aguacate"

# ----------------------------
# ORDENAMIENTO DE LISTAS
# ----------------------------
print("------------ORDENAMIENTO DE LISTAS------------")

print(frutas)  # Imprime la lista original
frutas.sort()  # Ordena la lista frutas en orden alfabético
print(frutas)  # Imprime la lista ordenada
numeros = [5, 2, 9, 1, 5, 6]  # Lista de números
numeros.sort()  # Ordena la lista de números en orden ascendente
print(numeros)  # Imprime la lista de números ordenada
frutas.sort(reverse=True)  # Ordena la lista frutas en orden alfabético inverso
print(frutas)  # Imprime la lista ordenada en orden inverso
numeros.sort(reverse=True)  # Ordena la lista de números en orden descendente
print(numeros)  # Imprime la lista de números ordenada en orden descendente
frutasMayusYMinus = ["Manzana", "pera", "Uva", "fresa", "mandarina"]
frutasMayusYMinus.sort(key=str.lower)  # Ordena la lista ignorando mayúsculas y minúsculas
print(frutasMayusYMinus)  # Imprime la lista ordenada ignorando mayúsculas y minúsculas
frutasMayusYMinus.reverse()  # Invierte el orden de los elementos en la lista
print(frutasMayusYMinus)  # Imprime la lista invertida

# ----------------------------
# COPIAS DE LISTAS
# ----------------------------
print("------------COPIAS DE LISTAS------------")
copiaFrutas = frutas.copy()  # Crea una copia superficial de la lista frutas
copiaFrutas3 = list(frutas)  # Crea una copia superficial de la lista frutas usando la función list()
frutasYNumeros = frutas + numeros  # Crea una nueva lista combinando frutas y números
print(frutasYNumeros)  # Imprime la lista combinada
frutasYNumeros2 = frutas.append(numeros)  # Añade la lista de números al final de la lista de frutas (modifica frutas)
