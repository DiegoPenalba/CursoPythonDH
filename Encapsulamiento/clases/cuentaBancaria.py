class CuentaBancaria:
    def __init__(self, titular, saldoInicial):
        self.__titular = titular # usando __ se hace privado el atributo
        self.__saldo = saldoInicial
    
    # Setter (configurador) de saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"deposito de ${cantidad} fue exitoso")
        else:
            print("ERROR: NO SE PUEDE DEPOSITAR UN SALDO NEGATIVO")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"se ha retirado {cantidad} exitosamente")
        else:
            print("Fondos insuficientes o cantidad invalida")
    
    # Getter (obtener informacion privada por medio de un metodo publico)

    def obtenerSaldo(self):
        return f"El saldo actual de la cuenta es: ${self.__saldo}"


    