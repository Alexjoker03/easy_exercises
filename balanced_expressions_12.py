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
    se_repite_2_en_1 = []
    
    #para llenar la lista 1 en 2
    for i in cadena_1:
        for j in cadena_2:
            if i == j:
                se_repite_1_en_2.append(i)

    
    
    
    #son las letras que se repiten de la cadena 1 en la 2
    se_repite_1_en_2 = set(se_repite_1_en_2)
    se_repite_1_en_2 = list(se_repite_1_en_2)
   
    #para pasar de lista a string
    s = ''.join(se_repite_1_en_2)
    print(f"estas son las letras que se repiten de la cadena 1 en la 2 {s}" )
    out_1 = 
    
                





cadena_1 = input("Escribe una palabra, frase u oración que te guste >>> ")
cadena_2 = input("Escribe otra palabra, frase u oración que te guste >>> ")

balanced_expressions(cadena_1, cadena_2)





