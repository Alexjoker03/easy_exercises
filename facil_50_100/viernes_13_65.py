"""---------------------------------------------------------------------
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
-----------------------------------------------------------------------"""
from datetime import datetime

año = int(input("DIgita el año en el que quieres buscar un VIERNES 13 >>> "))
mes = int(input("Digita el mes en el que quieres buscar un VIERNES 13 >>> "))
dia = 13
fecha_1 = datetime(año, mes, dia)   
fecha_1 = datetime.weekday(fecha_1)

if fecha_1 == 4:
    print(f"El año {año}, en el mes {mes} SÍ tiene VIERNES 13 =), no le abras la puerta a Jason")
else:
    print(f"El año {año}, en el mes {mes} NO tiene VIERNES 13, Jason no vendrá por ti")









