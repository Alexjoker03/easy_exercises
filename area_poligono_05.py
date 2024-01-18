""" ------------------------------------------------------------------
Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
--------------------------------------------------------------------"""

def area_poligono(opcion):
    # la opción 1 es triángulo
    if opcion == 1:
        base = int(input("¿Cuál es la base del triángulo: "))
        altura = int(input("¿Cuál es la altura del triángulo: "))
        area_triangulo = (base * altura) / 2
        return area_triangulo
    
    # la opción 2 es cuadrado
    elif opcion == 2:
        lado = int(input("¿Cuál es el lado del cuadrado: "))
        area_cuadrado = lado * lado
        return area_cuadrado
    
    # la opción 3 es rectángulo
    elif opcion == 3:
        lado = int(input("¿Cuál es el lado del rectángulo: "))
        ancho = int(input("¿Cuál es el ancho del rectángulo: "))
        area_rectangulo = lado * ancho
        return area_rectangulo
    
    else:
        print("la opción no es valida, adiós")

    
print("1) Triángulo \n2) Cuadrado \n3) Rectángulo")
opcion = int(input("Digíte el número correspondiente al área del polígono \nque desee obtener "))
resultado = area_poligono(opcion)
print(f"El área es: {resultado}")

      



        


