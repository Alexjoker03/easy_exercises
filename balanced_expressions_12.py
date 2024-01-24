"""-------------------------------------------------------------------
Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
----------------------------------------------------------------------"""

def balanced_expressions(cadena_1, cadena_2):
    se_repite_1_en_2 = []
    for i in cadena_1:
        for j in cadena_2:
            if i == j:
                se_repite_1_en_2.append(j)
    
    #para pasar de lista a string
    s = ''.join(se_repite_1_en_2)
    print(s)
                





cadena_1 = input("Escribe una palabra, frase u oración que te guste >>> ")
cadena_2 = input("Escribe otra palabra, frase u oración que te guste >>> ")

balanced_expressions(cadena_1, cadena_2)





