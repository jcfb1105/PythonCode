students = {'a': {'name':'Juan','notas':[3.1,4.2,4,3.9,3.2]}, 'j': {'name':'Jenny','notas':[4,3.7,4,4,4.2]},\
        'c': {'name':'Ana','notas':[4.1,4.7,4.1,4.9,4.2]}, 'y': {'name':'Pedro','notas':[4,3.7,4,4,4.2]},\
            'x': {'name':'Pablo','notas':[4,3.3,3.4,3.2,3.2]}, 'l': {'name':'Carlos','notas':[3.4,3.8,4.2,4,4.1]},\
                'v': {'name':'Maria','notas':[4.8,4.7,4.6,4.9,4.8]}, 'r': {'name':'Luisa','notas':[4.8,4.7,4.5,4.5,4.9]},\
                    'b': {'name':'Mario','notas':[2.4,3.2,3.1,3.4,4.2]}, 'g': {'name':'Fabio','notas':[2.4,3.2,3.1,3.4,4.2]}}

# El promedio mas alto high_average con nombre y promedio
# El promedio mas bajo low_average con nombre y promedio
# La nota mas alta de todas
# La nota mas baja de todas
# True o False si hay notas repetidas

# def high_average(students):
#     prom_mayor = 0
#     for student in students.values():
#         prom_stud = sum(student['notas']) / len(student['notas'])
#         if prom_stud > prom_mayor:
#             prom_mayor = prom_stud
#     print ("El promedio más alto es: " + str (prom_mayor))

promediomayor=0
promediomenor=100
notamayor=0
notamenor=100
for key, value in students.items():
    # print(value['name'])
    promedio=sum(value['notas'])/len(value['notas'])
    for n in value['notas']:
        if n>notamayor:
            notamayor=n
            snmayor=value['name']
        if n<notamenor:
            notamenor=n
            snmenor=value['name']
    # print(promedio)
    if promedio>promediomayor:
        promediomayor=promedio
        smayor=value['name']
    if promedio<promediomenor:
        promediomenor=promedio
        smenor=value['name']
            
print('El/la estudiante con promedio mayor es '+ str(smayor)+ ' con la nota '+ str(promediomayor))    
print('El/la estudiante con promedio menor es '+ str(smenor)+ ' con la nota '+ str(promediomenor))
print('la nota mayor es ' + str(notamayor)+' de '+ str(snmayor))
print('la nota menor es ' + str(notamenor)+' de '+str(snmenor))

print(students['x']['notas'].count(3.2))

  