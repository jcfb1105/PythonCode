# palindromo en forma de funcion

def palindromo(word):
    word = word.lower().replace(" ","")
    if word == word[::-1]:
        return f"¨{word} es palindromo"
    else:
        return f"{word} no es palindromo"


# print(palindromo("oso"))
# print(palindromo("Ana"))
# print(palindromo("Luz azul"))
# print(palindromo("Anita lava la tina"))

#-------------------------------------------------------------
# palindromo en lambda

es_palindromo = lambda word : "Si es" if word.lower().replace(" ","") == word.lower().replace(" ","")[::-1] else  "No es" 

print(es_palindromo("la tele letal"))

#-------------------------------------------------------------
# num1 es mayor que num2
verificar_mayor = lambda num1, num2: "Numero 1 es mayor" if num1 > num2 else "Numero 2 es mayor"
print(verificar_mayor(3,4)) 

#-------------------------------------------------------------
# el triple del primero es igual al doble de la raiz del segundo

verificar_condicion = lambda num1, num2: "Si es igual " if num1*3 == 2*num2**0.5 else "No es igual"
print(verificar_condicion(6, 81))