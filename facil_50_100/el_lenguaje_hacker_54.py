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
    "f":"|=",
    "g":"&",
    "j":",_|",
    "k":">|",
    "l":"1",
    "n":"^/",
    "ñ":"n/a",
    "m":"/\/\ ",
    "r":"I2",
    "h":"#",
    "i":"1",
    "o":"0",
    "p":"|*",
    "q":"(_,)",
    "r":"|2",
    "s":"5",
    "t":"7",
    "u":"(_)",
    "v":"\/",
    "w":"\/\/",
    "x":"><",
    "y":"j",
    "z":"2"

}



nuevo_string =[] 
alfabeto_normal = input("Escribe la oración que quieras pasar a lenguaje hacker >>> ")
alfabeto_normal = alfabeto_normal.lower()

#This is a solution using a list to collect the hacker characters

for i in range(len(alfabeto_normal)):
    if alfabeto_normal[i] in lenguaje_hacker:
        nuevo_string.append(lenguaje_hacker[alfabeto_normal[i]])
    else:
        nuevo_string.append(alfabeto_normal[i])    




resultado =''.join(nuevo_string)    
print(f"Este es el resultado con list {resultado}")   
 



