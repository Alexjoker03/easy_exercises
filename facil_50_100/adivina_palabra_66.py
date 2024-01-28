"""----------------------------------------------------------------------------------------------
Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
-----------------------------------------------------------------------------------------------"""
#cosas nuevas que aprendí
#list.index(elemento_a_buscar) = busca que posición dentro de una lista tiene un elemento
#import random
#random.choice(lista o tupla de la cual va a elegir) = elige un elemento aleatorio de una lista
import random

word = ["Toy Story", "Monsters inc", "El Lorax", "Mulan", "Star Wars"]
word_missing = ["T__ St_r_", "M_n__er_", "El L__a_", "M___n", "St__ W___"]
word_to_guess = random.choice(word_missing)
index_position = word_missing.index(word_to_guess)


print(f"Completa el nombre de la película \n{word_to_guess}")
letter_or_phrase = int(input("Quieres adivinar la palabra o adivinar una letra \nPresiona 1 para palabra o 2 para letra >>> "))
if letter_or_phrase == 1:
    choice_to_win = input("¿Qué película es? ")
    if choice_to_win == word[index_position]:
        print("Muy listo, correcto")
    else:
        print("No correcto, dude")
elif letter_or_phrase == 2:
    choice_letter = input("¿Qué letra crees que está presente en el nombre de la película? >>> ")
    
    if choice_letter in word[index_position]:
        for i in word[index_position]:

            if i == choice_letter:
                positions_for_letter_to_be_replace = int(word[index_position].index(i))

                #busco que index position para poder cambiar la letra
                #cambia todo
                word_missing_total = word_missing[index_position]
                word_missing_total = word_missing_total.replace(word_missing_total[positions_for_letter_to_be_replace], choice_letter)
                
                print(word_missing_total)




"""
            index_letter_position = word.index(choice_letter)
            word_missing[index_position] = word_missing[index_position].replace("_", choice_letter) 
            print(word_missing[index_position])   
"""
    





