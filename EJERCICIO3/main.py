from ejercicio3 import *

def iniciar():

    lista= crear_naves()

    #mostramos informacion de Millenium Falcon
    print("Mostramos informacion de Millenium Falcon")
    print(lista[0].nombre, lista[0].largo, lista[0].tripulacion, lista[0].pasajeros)

    #mostramos informacion de Death Star
    print("Mostramos informacion de Death Star")
    print(lista[2].nombre, lista[2].largo, lista[2].tripulacion, lista[2].pasajeros)

    #determinar cuáles son las cinco naves con mayor cantidad de pasajeros
    print("Las cinco naves con mayor cantidad de pasajeros son:")
    naves_mayor_pasajeros(lista)

    #determinar cuáles son las cinco naves con mayor cantidad de tripulación
    print("Las cinco naves con mayor cantidad de tripulacion son:")
    naves_mayor_tripulacion(lista)

    #determinar cuáles son las naves que empiezan con la letra A o T
    print("Las naves que empiezan con la letra A o T son:")
    naves_empiezan_AT(lista)

    #determinar cuáles son las naves que tienen más de seis pasajeros
    print("Las naves que tienen mas de seis pasajeros o 6 pasajeros son:")
    naves_mas_de_seis_pasajeros(lista)

    #determinar cuál es la nave más pequeña
    print("La nave mas pequeña es:")
    nave_mas_pequena(lista)

    #determinar cuál es la nave más grande
    print("La nave mas grande es:")
    nave_mas_grande(lista)


    #ordenar las naves por nombre de forma ascendente
    print("Las naves ordenadas por nombre de forma ascendente son:")
    ordenar__naves_por_nombre_ascedente(lista)
    mostrar_nave(lista)

    #ordenar las naves por nombre de forma descendente
    print("Las naves ordenadas por nombre de forma descendente son:")
    ordenar__naves_por_nombre_descendente(lista)
    mostrar_nave(lista)

