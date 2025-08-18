# ------------FUNCIONES DE ORDEN SUPERIOR----------------
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números del 1 al 10

# ------------MAP----------------

def cuadrado(x):
    return x * x
cuadrados = list(map(cuadrado, numeros)) # Aplica la función cuadrado a cada elemento de la lista numeros
print(cuadrados)

# ------------FILTER----------------
def es_par(x):
    return x % 2 == 0  # Devuelve True si el número es par, False si es impar

numeros_pares = list(filter(es_par, numeros))  # Filtra los números pares de la lista numeros
print(numeros_pares)