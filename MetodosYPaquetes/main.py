from calculos import operacionesMatematicas, funcionesAuxiliares

resultado = operacionesMatematicas.suma(5, 3)

print("Resultado de la suma:", resultado)

esPar = funcionesAuxiliares.esPar(4)
print("¿El número es par?", esPar)

divisionPorCero = operacionesMatematicas.division(10, 0)
print("Resultado de la división:", divisionPorCero)