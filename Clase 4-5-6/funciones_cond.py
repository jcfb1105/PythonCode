# edad1 = int (input("Escrine edad 1: "))
# edad2 = int (input("Escrine edad 2: "))
# edad3 = int (input("Escrine edad 3: "))
# edad4 = int (input("Escrine edad 4: "))

# def verificar_mayor(edad1, edad2, edad3, edad4):
#     if edad1 > edad2 and edad1 > edad3 and edad1 > edad4:
#         print(edad1)
#     elif edad2 > edad1 and edad2 > edad3 and edad2 > edad4:
#         print(edad2)
#     elif edad3 > edad1 and edad3 > edad2 and edad3 > edad4:
#         print(edad3)
#     else:
#         print(edad4)

def verificar_mayor(edad1, edad2, edad3, edad4):

    if edad1 >= edad2 >= edad3 >= edad4:
        print("1 " + str(edad1))
    elif edad2 > edad3 > edad4:
        print("2 " + str(edad2))
    elif edad3 > edad4:
        print("3 " + str(edad3))
    else:
        print("4 " + str(edad4))

# verificar_mayor(48, 48, 45, 45)
# verificar_mayor(65, 58, 45, 65)
verificar_mayor(12, 3, 4, 6)