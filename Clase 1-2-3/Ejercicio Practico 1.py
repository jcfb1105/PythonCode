"""
    Un bus viaja a 30km/h en promedio, 90km
    recoger pasajeros demora 2 minutos por pasajero
    bajar pasajero demora 1 minuto

    Cuantos minutos demora el bus, dada una cantidad de pasajeros que se subieron
    y otra cantidad de pasajeros que se bajaron
"""

numero_abordados = float(input("Numero de pasajeros que abordan: "))
numero_desc = float(input("Numero de pasajeros que descienden: "))

def calcular_tiempo(numero_abordados, numero_desc):
    duracion_estimada_viaje = (90/30)*60
    minutos_demora = duracion_estimada_viaje+((numero_abordados*2))+((numero_desc))
    return minutos_demora

print(calcular_tiempo(numero_abordados, numero_desc))