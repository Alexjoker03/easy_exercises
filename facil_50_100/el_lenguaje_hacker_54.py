"""------------------------------------------------------------------------------
Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

--------------------------------------------------------------------------------"""

lenguaje_hacker = {
    "a":"4",
    "b":"I3",
    "c":"[",
    "d":")",
    "e":"3",
    "m":"/\/\ ",
    "r":"I2",
    "h":"#",
    "i":"1",
    "o":"0"
}



nuevo_string =[] 
alfabeto_normal = input("Escribe la oración que quieras pasar a lenguaje hacker >>> ")
"""
frase_lista = []
for i in alfabeto_normal:
    frase_lista.append(i)

print(frase_lista)
for i in range(len(frase_lista)):
    if frase_lista[i]  == "a":
        frase_lista[i] = "$$"
    elif frase_lista[i] == "b":
        frase_lista[i] = "%&"

print(frase_lista)     
s = ''.join(frase_lista)
print(s)
"""



for i in range(len(alfabeto_normal)):
    if alfabeto_normal[i] in lenguaje_hacker:
        nuevo_string.append(lenguaje_hacker[alfabeto_normal[i]])
        alfabeto_normal = alfabeto_normal.replace(alfabeto_normal[i], lenguaje_hacker[alfabeto_normal[i]])

    else:
        pass


resultado =''.join(nuevo_string)    
print(resultado)   
print(alfabeto_normal) 



