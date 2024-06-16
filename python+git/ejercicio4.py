#Ejercicio 4
'''
Crea un juego de adivinar el número:
Escribe un programa que genere un número aleatorio entre 1 y 100.
El usuario debe intentar adivinar el número.
El programa debe proporcionar pistas como "más alto" o "más bajo" hasta que el usuario adivine correctamente.
Utiliza un bucle while para continuar pidiendo al usuario un número hasta que adivine correctamente.
'''

import random

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

while True:

    try:
        numero = int(input("ingrese un numero "))

        if numero < numero_aleatorio:
            print("el numero que debes adivinar es mayor que el que ingresaste")

        elif numero > numero_aleatorio:
            print("el numero que debes adivinar el menor al numero que ingresaste")

        else :
            print("felicidades adivinaste")    
    except:
        print("ingresa el valor correcto")        