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
    naves.append(Nave("Halcon Milenario", 34.37, 4, 6))
    naves.append(Nave("Ejecutor", 19000, 40000, 38000)) 
    naves.append(Nave("Estrella de la Muerte", 120000, 342953, 1000000))
    naves.append(Nave("Esclavo 1", 21.5, 1, 6)) 
    naves.append(Nave("Nave imperial", 20, 6, 20)) 
    

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
    for nave in lista:
        if nave.pasajeros > mayor.pasajeros:
            mayor= nave
    print('La nave {} tine un total de {} pasajeros'. format(mayor.nombre, mayor.pasajeros))



def naves_mayor_tripulacion(lista):
    mayor= lista[0]

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



