'''
float: nos permitira pasar un texto en un numero
base: numero que se dijita
altura: numero que se dijita
area: resultado de la base por el area dividido en 2
{} = plasehorlder en el cual se pondra el resultado de area
format(area) va seguidp de {} para asi poder poner el resultado del area dentro del plaseholder
runt
'''

base = float(input('Digite la base del triángulo: '))
altura = float(input('Digite la altura del triángulo: '))

area = base * altura / 2

print('El área del triángulo es igual a {}.'.format(area))