num1 = 15
num2 = 43

mensaje = "Los numeros son "+str(num1)+","+str(num2)
print(mensaje)
mensaje = "Los numeros son {},{}".format(num1,num2)
print(mensaje)
mensaje = "Los numeros son {1},{0},{2}".format(num1,num2,58)
print(mensaje)
mensaje = "Los numeros son %d, %d"%(num1,num2)
print(mensaje)
mensaje = f"Los numeros son {num1}, {num2}"
print(mensaje)


