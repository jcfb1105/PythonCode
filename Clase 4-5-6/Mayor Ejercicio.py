numeros1 = [59, 58+5, 45-5, 12*2]
numeros2 = [54, 58+5, 45, 12+24]
numeros3 = [54+2, 58+5, 45, 12]
numeros4 = [4, 58+5, 45*2, 12]

#Cual es el promedio mas alto dentro de los elementos

# prom1 = sum(numeros1)/len(numeros1)
# prom2 = sum(numeros1)/len(numeros2)
# prom3 = sum(numeros1)/len(numeros3)
# prom4 = sum(numeros1)/len(numeros4)

# def promedio(prom1, prom2, prom3, prom4):

#     if prom1 > prom2 and prom1 > prom3 and prom1 > prom4:
#         print(prom1)
#     elif prom2 > prom3 and prom2 > prom4:
#         print(prom2)
#     elif prom3 > prom4:
#         print(prom3)
#     else:
#         print(prom4)

def mayor(v1, v2 ,v3 ,v4):
    if v1 >= v2 and v1 >= v3 and v1 >= v4 :
        print('numeros1')
    elif v2 >= v3 and v2 >= v4 :
        print('numeros2')
    elif  v3 >= v4 :
        print('numeros3')
    else :
        print('numeros4')
def prom(numeros):
    return sum(numeros)/4
mayor(prom(numeros1), prom(numeros2), prom(numeros3), prom(numeros4))


