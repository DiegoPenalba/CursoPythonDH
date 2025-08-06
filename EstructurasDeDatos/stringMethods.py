texto = "hoLa muNdo"
textoConEspacios = "   Texto con espacios   "
textoSeparado = "Texto separado por comas, puntos y comas; y espacios"
lista = ["manzana", "banana", "cereza"]
textoNumerico = "12345"
letras = "abcde"
espacios = "   "
repeticion = "Manzana, Naranja, Manzana, Pera"

print(texto.capitalize())  # Convierte la primera letra a mayúscula y el resto a minúsculas
print(texto.lower())       # Convierte todo el texto a minúsculas
print(texto.upper())       # Convierte todo el texto a mayúsculas
print(textoConEspacios.strip())  # Elimina espacios al inicio y al final del texto
print(texto.replace(" ", "_"))  # Reemplaza espacios por guiones bajos
print(textoSeparado.split(", "))  # Divide el texto en una lista usando coma como separador
print(textoSeparado.split("; "))  # Divide el texto en una lista usando punto y coma como separador
print(textoSeparado.split())  # Divide el texto en una lista usando espacios como separador
print(",".join(lista))  # Une los elementos de la lista en un texto separado por comas
print(texto.find("muNdo"))  # Busca la subcadena "muNdo" y devuelve su índice
print(texto.index("muNdo"))  # Busca la subcadena "muNdo" y devuelve su índice (lanza error si no se encuentra
print(texto.rfind("muNdo"))  # Busca la subcadena "muNdo" desde el final y devuelve su índice
print(texto.startswith("hoLa"))  # Comprueba si el texto comienza con "hoLa"
print(texto.endswith("mundo"))  # Comprueba si el texto termina con "mundo"
print(letras.isalpha())  # Comprueba si todos los caracteres son alfabéticos
print(textoNumerico.isdigit())  # Comprueba si todos los caracteres son dígitos
print(letras.isalnum())  # Comprueba si todos los caracteres son alfanuméricos
print(espacios.isspace())  # Comprueba si todos los caracteres son espacios en blanco
print(repeticion.count("Manzana"))  # Cuenta cuántas veces aparece "Manzana" en el texto
