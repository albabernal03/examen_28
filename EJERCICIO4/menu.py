from ejercicio4 import *


def iniciar():
    print('1. Restar')
    print('2. Dividir')
    print('3. eliminar termino')
    print('4.Determinar si un termino existe en el polinomio')

    opcion= int(input('Ingrese una opcion: '))
    polinomio= Polinomio()


    if opcion==1:
        p1= Polinomio()
        p2= Polinomio()

        agregar_termino(p1,2,3)
        agregar_termino(p1,1,2)
        agregar_termino(p1,0,1)

        agregar_termino(p2,3,1)
        agregar_termino(p2,1,2)
        agregar_termino(p2,0,3)

        print('Polinomio 1: ',mostrar_polinomio(p1))
        print('Polinomio 2: ',mostrar_polinomio(p2))

        p3= restar(p1,p2)

        print('Resta: ',mostrar_polinomio(p3))


    elif opcion==2:
        p1= Polinomio()
        p2= Polinomio()

        agregar_termino(p1,2,3)
        agregar_termino(p1,1,2)
        agregar_termino(p1,0,1)

        agregar_termino(p2,3,1)
        agregar_termino(p2,1,2)
        agregar_termino(p2,0,3)

        print('Polinomio 1: ',mostrar_polinomio(p1))
        print('Polinomio 2: ',mostrar_polinomio(p2))

        p3= dividir(p1,p2)

        print('Division: ',mostrar_polinomio(p3))

    elif opcion==3:
        p1= Polinomio()
        agregar_termino(p1,2,3)
        agregar_termino(p1,1,2)
        agregar_termino(p1,0,1)
        print('Polinomio 1: ',mostrar_polinomio(p1))
        eliminar_termino(p1,2)
        print('Polinomio 1: ',mostrar_polinomio(p1))

    elif opcion==4:
        p1= Polinomio()
        agregar_termino(p1,2,3)
        agregar_termino(p1,1,2)
        agregar_termino(p1,0,1)
        print('Polinomio 1: ',mostrar_polinomio(p1))
        print('Existe el termino: ',existe_termino(p1,2))

 