""" -------------------------------------------------------------------------
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
--------------------------------------------------------------------------"""

cadena = input("Escribe una palabra, frase u oración y te la devolveré a la inversa: ")
cadena_backwards = len(cadena)
inicio = int(cadena_backwards - 1)
fin = int(cadena_backwards * -1)

print(cadena[::-1])

print(cadena[inicio:fin-1:-1])
