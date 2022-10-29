class nodoNave:
    info, sig= None, None

class Nave:
    def __init__(self, nombre, largo, tripulacion, pasajeros):
        self.nombre= nombre
        self.largo= largo
        self.tripulacion= tripulacion
        self.pasajeros= pasajeros

def crear_naves():
    naves= []
    naves.append(Nave("Millenium Falcon", 34.37, 4, 6))
    naves.append(Nave("Executor", 19000, 40000, 38000))
    naves.append(Nave("Death Star", 120000, 342953, 1000000))
    naves.append(Nave("Slave 1", 21.5, 1, 6))
    naves.append(Nave("Imperial shuttle", 20, 6, 20))
    

    return naves

def ordenar__naves_por_nombre_ascedente(lista): # hemos aplicado el metodo de ordenamiento por seleccion
    print('Las naves ordenadas por nombre de forma ascendente son:')
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i].nombre > lista[j].nombre:
                lista[i], lista[j] = lista[j], lista[i]


def ordenar__naves_por_nombre_descendente(lista): # hemos aplicado el metodo de ordenamiento por seleccion
    print('Las naves ordenadas por nombre de forma descendente son:')
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i].nombre < lista[j].nombre:
                lista[i], lista[j] = lista[j], lista[i]


def mostrar_nave(lista):
    for nave in lista:
        print(nave.nombre, nave.largo, nave.tripulacion, nave.pasajeros)


def naves_mayor_pasajeros(lista):
    mayor= lista[0]
    for i in range(5):
        for nave in lista:
            if nave.pasajeros > mayor.pasajeros:
                mayor= nave
        print(mayor.nombre, mayor.largo, mayor.tripulacion, mayor.pasajeros)



def naves_mayor_tripulacion(lista):
    mayor= lista[0]
    for i in range(5):
        for nave in lista:
            if nave.tripulacion > mayor.tripulacion:
                mayor= nave
        print(mayor.nombre, mayor.tripulacion)


def naves_empiezan_AT(lista):
    for nave in lista:
        if nave.nombre[0] == "A" or nave.nombre[0] == "T":
            print(nave.nombre)


def naves_mas_de_seis_pasajeros(lista):
    for nave in lista:
        if nave.pasajeros >= 6:
            print(nave.nombre,nave.pasajeros)


def nave_mas_pequena(lista):
    menor= lista[0]
    for nave in lista:
        if nave.largo < menor.largo:
            menor= nave
    print(menor.nombre, menor.largo)

def nave_mas_grande(lista):
    mayor= lista[0]
    for nave in lista:
        if nave.largo > mayor.largo:
            mayor= nave
    print(mayor.nombre, mayor.largo)



def main():

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
    print("Las naves que tienen mas de seis pasajeros son:")
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

main()
