print ("Bienvenido al sistema de ubicacion para zonas publicas WIFI")
nombre_de_usuario = int(51743)
contraseña = int(34715)
salida = "Error"

print ('Bienvenido al  sistema de ubicación para zonas publicas WIFI')
username = int(51743)
password = int(34715)
exit = 'Error' 
loginusername = int(input ('Por favor ingrese su usuario: '))
digcapcha1 = int(743)
digcapcha2 = int(5+1*7-(7%5)**3)
if loginusername == username:
    loginpassword = int(input ('Por favor ingrese su password: '))
    if loginpassword == password:
        print(digcapcha1, ' + ', digcapcha2)

        capcha = int(input('Por favor ingrese el valor de la suma: ' ))
        
        if capcha == digcapcha1 + digcapcha2:
            print('Sesion iniciada')
        else:
            print(exit)    

    else:
        print(exit)   

else:
    print(exit) 
