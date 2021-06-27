numeros = [3.1, 2.8, 4.2, 4, 3.9, 2.78, 3.2, 3.68, 4.01, 2.99]
lista = [5, 4, 6, 8, 9, 1, 7, 3, 6, 8, 5]

filter_function = lambda numero: numero < 3

filtrado = list(filter (filter_function,numeros))
print(filtrado)

#----------------------------------------------------------
#sacar pares con filtro

filtrar_pares = lambda lista: lista % 2 == 0

pares = list(filter(filtrar_pares, lista))
print(pares)

#----------------------------------------------------------
#Sacas impares con filtro

filtrar_impares = lambda lista: lista % 2 != 0

impares = list(filter(filtrar_pares, lista))
print(pares)

#---------------------------------------------------------


