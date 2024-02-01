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

lives = 3
word = ["Toy Story", "Monsters inc", "El Lorax", "Mulan", "Star Wars"]
word_missing = ["T__ St_r_", "M_n__er_ _n_", "El L__a_", "M___n", "St__ W___"]
word_to_guess = random.choice(word_missing) 
index_position = word_missing.index(word_to_guess)
word_to_compare_to = word[index_position]

word_to_guess_2 = []
for i in word_to_guess:
    word_to_guess_2.append(i)

word_to_compare_to_2 = []
for i in word_to_compare_to:
    word_to_compare_to_2.append(i)





while lives >= 1:
    print(f"Completa el nombre de la película \n{word_to_guess}")
    print(f"Tienes {lives} oportunidades para adivinar ")
    letter_or_phrase = int(input("Quieres adivinar la palabra o adivinar una letra \nPresiona 1 para palabra o 2 para letra >>> "))
    if letter_or_phrase == 1:
        choice_to_win = input("¿Qué película es? ")
        if choice_to_win == word_to_compare_to:
            print("Muy listo, correcto")
            lives = 0
        else:

            print("No correcto, dude")
            lives = lives - 1
            print(f"Te quedan {lives} vidas, cuidadito Wazauski")
            if lives == 0:
                print("ya se ti acabaron las vidas, adiós")
                break

    elif letter_or_phrase == 2:
        choice_letter = input("¿Qué letra crees que está presente en el nombre de la película? >>> ")
    
        if choice_letter in word_to_compare_to:
        
            position_in_word = -1
            for i in word_to_compare_to_2:
                position_in_word = word_to_compare_to_2.index(i, position_in_word + 1)
                
                if i == choice_letter:
                    word_to_guess_2[position_in_word] = i
                   
        else:
            lives = lives - 1

        word_to_guess = ''.join(word_to_guess_2)  
        if word_to_guess_2 == word_to_compare_to_2:
            print("Eres muy listo, adivinaste la película")
            lives = 0  

                
                   
    
        





    





