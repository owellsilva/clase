'''
float: nos permite pasar de texto a numero
{} = plasehorlder en el cual se pondra el resultado de area
format(nota) va seguido de {} para asi poder poner el resultado del area dentro del plaseholder
nota = resultado final de la suma de todas las notas obtenidas
'''


reto_nota1 = float(input (' ingrese la nota numero 1: '))
reto_nota2 = float(input (' ingrese la nota numero 2: '))
reto_nota3 = float(input (' ingrese la nota numero 3: '))
ingles = float(input (' ingrese la nota de ingles: '))

nota = reto_nota1*0.2 + reto_nota2*0.25 + reto_nota3*0.35 + ingles*0.2 

print('la nota definitica del estudiante es:', format(nota)) 