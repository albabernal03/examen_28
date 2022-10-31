from ejercicio4 import *


def iniciar():
    print('1. Agregar termino')
    print('2. Eliminar termino')
    print('3. Modificar termino')
    print('4. Obtener valor de un termino')
    print('5. Mostrar polinomio')
    print('6. Sumar polinomios')
    print('7. Restar polinomios')
    print('8. Multiplicar polinomios')
    print('9. Dividir polinomios')
    print('10. Salir')

    opcion= int(input('Ingrese una opcion: '))
    polinomio= Polinomio()


    if opcion==6:
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

        p3= sumar(p1,p2)

        print('Suma: ',mostrar_polinomio(p3))

    elif opcion==7:
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


    elif opcion==8:
        
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

        p3= multiplicar(p1,p2)

        print('Multiplicacion: ',mostrar_polinomio(p3))

    elif opcion==9:
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


    elif opcion==10:
        print('Hasta luego!')
        exit()

    else:
        print('Opcion invalida')

    iniciar()

 