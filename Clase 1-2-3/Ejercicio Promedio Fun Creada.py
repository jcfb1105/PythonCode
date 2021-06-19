def calcular_total(num1:float, num2:float, num3:float) -> float:
    total_local = num1+num2+num3
    return total_local

def promedio():
    numero_1 = float(input("Primer numero: "))
    numero_2 = float(input("Segundo numero: "))
    numero_3 = float(input("Tercer numero: "))
    total = calcular_total(numero_1,numero_2,numero_3)
    return  total/3

print("Promedio es: "+str(promedio()))