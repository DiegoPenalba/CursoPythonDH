def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    try: 
        resultado = a / b
    except ZeroDivisionError:
        return "Error: División por cero no permitida." 
    return resultado
