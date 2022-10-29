from ejercicio4 import *


p1= Polinomio()
p2= Polinomio()

agregar_termino(p1,2,3)
agregar_termino(p1,1,2)
agregar_termino(p1,0,1)

agregar_termino(p2,2,1)
agregar_termino(p2,1,2)
agregar_termino(p2,0,3)

print('Polinomio 1: ',mostrar_polinomio(p1))
print('Polinomio 2: ',mostrar_polinomio(p2))

p3= sumar(p1,p2)

print('Suma: ',mostrar_polinomio(p3))