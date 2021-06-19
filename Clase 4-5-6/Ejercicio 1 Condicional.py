opcion = int (input('Escribe la edad: '))

if opcion >= 10 and opcion <= 14:
    print('Infantil')
elif opcion > 14 and opcion <= 17:
    print('Juvenil')
elif opcion > 17 and opcion <= 20:
    print("Sub 20")
elif opcion > 20:
    print('Profesional')
else:
    print('Opción invalida')