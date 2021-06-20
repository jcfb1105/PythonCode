palabra = "Una palabra"

lista = list(palabra)
print(palabra.split(" "))
print(palabra)
print(lista)

diccionario = {"nombre":"Lina","Apellido":"Silva"}
lista = list(diccionario.keys())
lista = list(diccionario.values())
#lista = list(diccionario.items())
print(lista)
tupla = tuple(lista)
print(tupla)
lista = list(palabra)
#print(dict(lista))
palabra = "".join(lista)
print(palabra)