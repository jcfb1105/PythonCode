edad = 58
genero = "F"
semanas = 240

if edad >= 58 and genero == "F" and semanas >= 250:
    print("Se puede pensionar")
else:
    print("No se puede pensionar")

if genero == "F":
    if  edad >= 50:
        if semanas >= 250:
            print("Se puede pensionar")
        else:
            print("Le faltan " + str (250 - semanas) + " semanas")
    else:
        print("Le faltan " + str (58 - edad)+ " años")

elif genero == "M":
    if edad >= 63:
        if semanas >= 250:
            print("Se puede pensionar")
        else:
            print("Le faltan " + str (250 - semanas)+ " semanas")
    else:
        print("Le faltan " + str (63 - edad)+ " años")

else:
    print("Indique M para masculino y F para femenino")
