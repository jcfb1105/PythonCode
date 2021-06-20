lista =[5,4,6,8]

matriz = [lista, lista, lista]
#indices    0      1      2
matriz = [[5,7,6,9],[3,4,2,8],[7,9,6,1]]

Lista1 = matriz[0]
Lista2 = matriz[1]
#matriz[1] = Lista1

Lista3 = matriz[2]

# print(matriz[0])
# print(matriz[0][0]) # Primer elemento de la primer lista
# print(matriz[1][0]) # Primer elemento de la segunda lista
# print(matriz[-1][-1]) # Ultimo elemento de la ultima lista
# matriz[-1][-1]=5 # Modificar ultimo elemento de una matriz y reemplazarla
# print(matriz[-1][-1])
# print(matriz)

i = 0
while i < len(matriz):
    print(matriz[i])
    j = 0
    while j < len(matriz[i]):
        if matriz[i][j] > 4:
            print(matriz[i][j])
        j+=1
    i+=1





# for fila in matriz:
#     print(max(fila))
#     print(min(fila))
#     print(sum(fila)/len(fila))
    