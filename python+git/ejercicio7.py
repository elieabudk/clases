'''
Agrupación de palabras por longitud:
Escribe un programa que tome una lista de palabras y las agrupe en un diccionario donde las claves 
son las longitudes de las palabras y los valores son listas de palabras de esa longitud.
'''
lista_palabras = ["cafe", "papas", "carne" ,"zanahria", "calabaza"]


grupo = {}

for palabras in lista_palabras:
    numero_letras  =  len(palabras)
    if numero_letras not in grupo:
        grupo[numero_letras]=[]
    grupo[numero_letras].append(palabras)

print(grupo)    


