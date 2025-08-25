from clases.mago import Mago

merlin = Mago("Merlin", ["Bola de fuego", "Rayo"])
gandalf = Mago("Gandalf", ["Llamar aguilas al termino de la pelicula", "Bola de fuego"])

print(merlin) ## Devuelve el metodo __str__ que se habia creado
print(len(merlin)) ## Devuelve el metodo __len__ que habiamos creado

print(gandalf)
print(len(gandalf))

print(merlin == gandalf)

copia_merlin = Mago("Merlin", ["Bola de fuego", "Rayo"])

print(merlin == copia_merlin) # Devuelve comparacion usando criterios definido en el metodo __eq__

mago_combinado = merlin + gandalf