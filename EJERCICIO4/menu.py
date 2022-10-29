from ejercicio4 import *


def menu():
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

    if opcion == 1:
        termino= int(input('Ingrese el termino: '))
        valor= int(input('Ingrese el valor: '))
        agregar_termino(polinomio,termino,valor)

    elif opcion == 2:
        termino= int(input('Ingrese el termino: '))
        eliminar_termino(polinomio,termino)

    elif opcion == 3:
        termino= int(input('Ingrese el termino: '))
        valor= int(input('Ingrese el valor: '))
        modificar_termino(polinomio,termino,valor)

    elif opcion == 4:
        termino= int(input('Ingrese el termino: '))
        print(obtener_valor(polinomio,termino))

    elif opcion == 5:
        print(mostrar_polinomio(polinomio))
        
    elif opcion == 6:
        polinomio2= Polinomio()
        polinomio3= sumar(polinomio,polinomio2)
        print(mostrar_polinomio(polinomio3))

    elif opcion == 7:
        polinomio2= Polinomio()
        polinomio3= restar(polinomio,polinomio2)
        print(mostrar_polinomio(polinomio3))

    elif opcion == 8:
        polinomio2= Polinomio()
        polinomio3= multiplicar(polinomio,polinomio2)
        print(mostrar_polinomio(polinomio3))
    
    elif opcion == 9:
        polinomio2= Polinomio()
        polinomio3= dividir(polinomio,polinomio2)
        print(mostrar_polinomio(polinomio3))

    elif opcion == 10:
        return


        



