def esPar(numero):
    return numero % 2 == 0

def esPrimo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
