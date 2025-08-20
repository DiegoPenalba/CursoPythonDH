from clases.cuentaBancaria import CuentaBancaria

cuenta = CuentaBancaria("Diego",1000)

# No se puede acceder a un atributo privado
# print(cuenta.__saldo)

# No se puede sobreescribir un dato
# cuenta.__titular = "ricardito"

# obtener saldo inicial
print(cuenta.obtenerSaldo())

# Deposito plata y obtengo saldo
cuenta.depositar(500)
print(cuenta.obtenerSaldo())

# Retiro dinero y obtengo saldo
cuenta.retirar(1500)
print(cuenta.obtenerSaldo())

# Error al depositar
cuenta.depositar(-100)
print(cuenta.obtenerSaldo())

# Error al retirar
cuenta.retirar(100)
print(cuenta.obtenerSaldo())