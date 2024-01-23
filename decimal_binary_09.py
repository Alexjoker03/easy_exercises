"""----------------------------------------------------------------------------------------
Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
-------------------------------------------------------------------------------------------"""

number = int(input("What number do you want to convert into a binary number?  "))
binary_number_list = []

while number >= 1:

    if number % 2 == 1:
        binary_number_list.append(1)
        number = (number / 2) - 0.5
    elif number % 2 == 0:
        binary_number_list.append(0)
        number = number / 2

print(binary_number_list[::-1])






