'''
Eliminación de elementos duplicados de una lista:
Crea una lista que contenga elementos duplicados.
Escribe una función que elimine los elementos duplicados de la lista y devuelva una nueva lista sin duplicados.
Utiliza un bucle anidado y una tupla para comparar cada elemento con los demás.
Ejemplo:

Salida: [1, 2, 3, 4, 5]
'''

Lista= [1, 2, 2, 3, 4, 4, 5]
salida = []

for i in Lista:
    if i not in salida:
        salida.append(i)

print(salida)        