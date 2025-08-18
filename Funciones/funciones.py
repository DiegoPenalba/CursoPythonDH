# ----------------------------
# FUNCIONES EN PYTHON
# ----------------------------

def saludar(nombre, apellido, apodo=""):
    """Función que saluda a una persona por su nombre."""
    print(f"Hola, {nombre} {apodo} {apellido}!")

saludar("Diego", "Penalba")  # Llama a la función saludar con el nombre "Diego". 
#Sino se pone nada,no funciona, porque le falta el parametro. Para solucionarlo, se le puede poner un valor por defecto al parametro apodo.
# o un * delante del parametro apodo, para que sea opcional.

def saludar2(nombre, apellido, *apodo): 
    """Función que saluda a una persona por su nombre y apodo."""
    print(f"Hola, {nombre} {apodo} {apellido}!")

saludar2("Diego", "Penalba", "El Capo")  # Llama a la función saludar2 con el nombre "Diego" y el apodo "El Profe".
saludar2("Diego", "Penalba")  # Llama a la función saludar2 con el nombre "Diego" y sin apodo.

def soloNombre(*nombres):
    if len(nombres) > 1:  # Comprueba si no se ha pasado ningún nombre
        print(f"Hola, {nombres[0]}, {nombres[1]}!")  # Imprime el primer nombre de la lista de nombres
    else:
        print(f"Hola, {nombres[0]}")

soloNombre("Diego", "Penalba")  # Llama a la función soloNombre con los nombres "Diego" y "Penalba".
soloNombre("Diego")  # Llama a la función soloNombre con el nombre "Diego".

def padreOrgulloso(hijo1, hijo3, hijo2):
    """Función que imprime los nombres de los hijos."""
    print(f"Mis hijos son: {hijo1}, {hijo2}, {hijo3}")
    print (f"Mi hijo mas pequeño es: {hijo3}")

padreOrgulloso("Diego", "Pepe", "Peppo")
padreOrgulloso(hijo1="Diego", hijo2="Pepe", hijo3="Peppo")  # Llama a la función padreOrgulloso con los nombres de los hijos.


def mostrarMercaderia(mercaderia):
    """Función que imprime la mercadería."""
    for producto in mercaderia:  # Recorre cada producto en la mercadería.
        print(f"Producto: {producto}")  # Imprime el nombre del producto

mercaderia = ["Manzana", "Pera", "Uva", "Fresa"]  # Lista de productos.
mostrarMercaderia(mercaderia)  # Llama a la función mostrarMercaderia con la lista de productos.




def suma(a, b):
    """Función que suma dos números."""
    resultado = a + b  # PARAMETROS) Dentro de la funcion
    return resultado

resultado = suma(5, 3)  # de forma global(ARGUMENTOS)

def sumaConParametrosPorDefecto(a=0, b=0):
    """Función que suma dos números con parámetros por defecto."""
    return a + b  # Devuelve la suma de los dos números.

def devolverCuadrado(numero):
    """Función que devuelve el cuadrado de un número."""
    return numero ** 2  # Devuelve el cuadrado del número.

print(devolverCuadrado(numero=2)) #keyword argument
print(devolverCuadrado(2))  # positional argument

def devolverCuadradoSinKeywordArgument(numero, /):
    return numero ** 2  # Devuelve el cuadrado del número sin permitir argumentos por palabra clave.

print(devolverCuadradoSinKeywordArgument(2))  # Llama a la función devolverCuadradoSinKeywordArgument con el número 2.
# print(devolverCuadradoSinKeywordArgument(numero=2))  # Esto lanzaría un error porque no se permiten argumentos por palabra clave. 

def devolverCuadradoPositionalArgument(*, numero):
    return numero ** 2  # Devuelve el cuadrado del número sin permitir argumentos posicionales.

print(devolverCuadradoPositionalArgument(numero=2))  # Llama a la función devolverCuadradoPositionalArgument con el número 2.
# print(devolverCuadradoPositionalArgument(numero=2))  # Esto lanzaría un error porque no se permiten argumentos posicionales.

def devolverCuadradoMix(numero, /, *, exponente):
    return numero ** exponente  # Devuelve el número elevado al exponente especificado.

print(devolverCuadradoMix(2, exponente=3))  # Llama a la función devolverCuadradoMix con el número 2 y el exponente 3.
# print(devolverCuadradoMix(numero=2, exponente=3))  # Esto lanzaría un error porque no se permiten argumentos por palabra clave para el número.

def operaciones(a,b):
    suma = a + b  # Suma de los dos números.
    resta = a - b  # Resta de los dos números.
    multiplicacion = a * b  # Multiplicación de los dos números.
    division = a / b if b != 0 else "Error: División por cero"  # División de los dos números, manejando la división por cero.
    return suma, resta, multiplicacion, division

resultado = operaciones(10, 5)  # Llama a la función operaciones con los números 10 y 5.
print(f"Suma: {resultado[0]}, Resta: {resultado[1]}, Multiplicación: {resultado[2]}, División: {resultado[3]}")  # Imprime los resultados de las operaciones.


# ----------------------------
# FUNCIONES RECURSION: Funciones que se llaman a sí mismas. Suplen los bucles en algunos casos.
# ----------------------------
print("------------FUNCIONES RECURSION------------")    
# ----------------------------

def factorial(n):
    """Función que calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:  # Caso base: el factorial de 0 o 1 es 1.
        return 1
    else:
        return n * factorial(n - 1)  # Llama a la función factorial con n-1 y multiplica por n.

print(factorial(5))  # Llama a la función factorial con el número 5 y muestra el resultado.

def fibonacci(n):
    """Función que calcula el n-ésimo número de Fibonacci de forma recursiva.
    La secuencia de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores.
    
    Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, ...

    Args:
        n (int): El índice del número de Fibonacci a calcular.

    Returns:
        int: El n-ésimo número de Fibonacci.    
    """
    if n <= 0:  # Caso base: si n es menor o igual a 0, devuelve 0.
        return 0
    elif n == 1:  # Caso base: si n es 1, devuelve 1.
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(2))  # Llama a la función fibonacci con el número 6 y muestra el resultado.

def deletreo(palabra):
    """Función que deletrea una palabra.
    Args:
        palabra (str): La palabra a deletrear.

    Returns:
        str: La palabra deletreada, con cada letra separada por un espacio.
    """
    if len(palabra) == 0:  # Si la palabra está vacía, termina la recursión.
        return ""
    else:
        return palabra[0] + " " + deletreo(palabra[1:])  # Deletrea la primera letra y llama a la función con el resto de la palabra.

print(deletreo("Python"))  # Llama a la función deletreo con la palabra "Python" y muestra el resultado.

print("------------FUNCIONES DOCUMENTACION------------")    

print(deletreo.__doc__)  # Imprime la documentación de la función deletreo.
help(fibonacci)  # Muestra la documentación de la función fibonacci.

print("------------FUNCIONES LAMBDA------------")    

def operaciones(operacion):
    if operacion == "suma":
        return lambda a, b: a + b  # Retorna una función lambda que suma dos números.
    elif operacion == "resta":
        return lambda a, b: a - b  # Retorna una función lambda que resta dos números.
    elif operacion == "multiplicacion":
        return lambda a, b: a * b  # Retorna una función lambda que multiplica dos números.
    else:
        return lambda a, b: a / b if b != 0 else "Error: División por cero"  # Retorna una función lambda que divide dos números, manejando la división por cero.

suma = operaciones("suma")  # Llama a la función operaciones con "suma" y asigna la función lambda resultante a suma.
resta = operaciones("resta")  # Llama a la función operaciones con "resta" y asigna la función lambda resultante a resta.
multiplicacion = operaciones("multiplicacion")  # Llama a la función operaciones con "multiplicacion" y asigna la función lambda resultante a multiplicacion.
division = operaciones("division")  # Llama a la función operaciones con "division" y asigna la función lambda resultante a division.

print(suma(5, 3))  # Imprime el resultado de la suma de 5 y 3.

diccionarioCualquiera = [
    {"Nombre": "Diego", "Edad": 30},
    {"Nombre": "Pepe", "Edad": 25},
    {"Nombre": "Peppo", "Edad": 20}     
]

estudiantesOrdenados = sorted(diccionarioCualquiera, key=lambda x: x["Edad"])  # Ordena la lista de diccionarios por la clave "Edad" usando una función lambda.
print(estudiantesOrdenados)  # Imprime la lista de diccionarios ordenada por edad.

# -----------CLOSURES----------------
print("------------CLOSURES------------")

def exterior(x):
    def interior(y):
        return x + y  # La función interior utiliza la variable x de la función exterior.
    return interior  # La función exterior retorna la función interior.

closure = exterior(10)  # Llama a la función exterior con el valor 10 y asigna la función interior resultante a closure.
print(closure(5))  # Llama a la función closure con el valor 5, lo que suma 10 + 5 y muestra el resultado.

# ----------- DECORATORS AND WRAPPERS----------------
print("------------DECORATORS AND WRAPPERS------------")    

def decorador(funcion):
    def envoltorio():
        print("Antes de llamar a la función")  # Imprime un mensaje antes de llamar a la función.
        funcion()  # Llama a la función original.
        print("Después de llamar a la función")  # Imprime un mensaje después de llamar a la función.
    return envoltorio  # Retorna la función envoltorio.

def saludo():
    print("¡Hola!")  # Imprime un saludo.

saludo_decorado = decorador(saludo)  # Aplica el decorador a la función saludo.
saludo_decorado()  # Llama a la función decorada, lo que ejecuta el envoltorio y la función original.
