'''
 Búsqueda de elementos en una matriz:
Crea una matriz (lista de listas) de números.
Escribe una función que busque un número específico en la matriz y devuelva su posición (fila, columna) si se encuentra, o None si no se encuentra.
Utiliza bucles anidados para recorrer la matriz y comprobar cada elemento.
Ejemplo:
Matriz: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Número a buscar: 5
Salida: (1, 1)
'''

Matriz= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

numero = int(input("ingrese el numero"))
numero_encontrado = False
for i in Matriz:
    lista= i
   
    for elemento in lista:
        if numero == elemento:
            indice = lista.index(elemento)
            indice2 = Matriz.index(i)
            print(f"{indice2} , {indice} ")
            numero_encontrado=True

if not numero_encontrado:
    print("no se encuentra el numero")
           



            