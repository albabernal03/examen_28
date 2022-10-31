class Nodo(object):
    info,sig= None,None

class datoPolinomio(object):
    ''''Clase que representa un dato de un polinomio'''
    def __init__(self, valor, termino):
        self.valor= valor
        self.termino= termino

class Polinomio(object):
    '''Clase que representa un polinomio'''
    def __init__(self):
        self.termino_mayor= None
        self.grado= -1


def agregar_termino(polinomio,termino,valor):
    aux=Nodo()
    dato= datoPolinomio(valor,termino)
    aux.info=dato
    if termino > polinomio.grado:
        aux.sig= polinomio.termino_mayor
        polinomio.termino_mayor= aux
        polinomio.grado= termino
    else:
        actual= polinomio.termino_mayor
        while actual.sig is not None and termino < actual.sig.info.termino:
            actual= actual.sig
        aux.sig= actual.sig
        actual.sig= aux

#ESTA ES UNA DE LAS FUNCIONES IMPLEMENTADAS
def eliminar_termino(polinomio,termino):
    if polinomio.termino_mayor is not None: #si el polinomio no esta vacio
        if polinomio.termino_mayor.info.termino == termino: #si el termino mayor es el que quiero eliminar
            polinomio.termino_mayor= polinomio.termino_mayor.sig #el termino mayor pasa a ser el siguiente
        else:
            actual= polinomio.termino_mayor #si no es el termino mayor, recorro la lista
            while actual.sig is not None and actual.sig.info.termino != termino: #mientras no sea el ultimo nodo y el termino del nodo siguiente no sea el que quiero eliminar
                actual= actual.sig #avanzo
            if actual.sig is not None: #si no llegue al final de la lista
                actual.sig= actual.sig.sig #el nodo actual apunta al nodo siguiente del nodo que quiero eliminar(eliminando asi el nodo que quiero eliminar)

def modificar_termino(polinomio,termino,valor):
    aux= polinomio.termino_mayor
    while aux is not None and aux.info.termino != termino:
        aux= aux.sig
    aux.info.valor= valor

def obtener_valor(polinomio,termino):
    aux= polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:
        aux= aux.sig
    if aux is not None and aux.info.termino == termino:
        return aux.info.valor
    else:
        return 0


def mostrar_polinomio(polinomio):
    aux= polinomio.termino_mayor
    pol= ''
    if aux is not None:
        while aux is not None:
            signo=''
            if aux.info.valor >= 0:
                signo='+'
            pol +=signo + str(aux.info.valor) + 'x^' + str(aux.info.termino)
            aux= aux.sig
        
    return pol


def sumar(polinomio1,polinomio2):
    paux= Polinomio()
    mayor= polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
    for i in range (0,mayor.grado+1):
        total= obtener_valor(polinomio1,i) + obtener_valor(polinomio2,i)
        if total != 0:
            agregar_termino(paux,i,total)
    return paux

#FUNCION AÑADIDA
def restar(polinomio1,polinomio2):
    paux= Polinomio()
    mayor= polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
    menor= polinomio1 if (polinomio1.grado < polinomio2.grado) else polinomio2
    for i in range (0,mayor.grado+1):
        total= obtener_valor(mayor,i) - obtener_valor(menor,i)
        if total != 0:
            agregar_termino(paux,i,total)
    return paux


def multiplicar(polinomio1,polinomio2):
    paux= Polinomio()
    pol1= polinomio1.termino_mayor
    while pol1 is not None:
        pol2= polinomio2.termino_mayor
        while pol2 is not None:
            termino= pol1.info.termino + pol2.info.termino
            valor=  pol1.info.valor * pol2.info.valor
            if obtener_valor(paux,termino) != 0:
                valor += obtener_valor(paux,termino)
                modificar_termino(paux,termino,valor)
            else:
                agregar_termino(paux,termino,valor)
            pol2= pol2.sig

        pol1= pol1.sig
    return paux

#FUNCION AÑADIDA

def dividir(polinomio1,polinomio2):
    paux= Polinomio()
    pol1= polinomio1.termino_mayor
    while pol1 is not None:
        pol2= polinomio2.termino_mayor
        while pol2 is not None:
            termino= pol1.info.termino + pol2.info.termino 
            valor=  pol1.info.valor / pol2.info.valor
            if obtener_valor(paux,termino) != 0:
                valor += obtener_valor(paux,termino)
                modificar_termino(paux,termino,valor)
            else:
                agregar_termino(paux,termino,valor)
            pol2= pol2.sig

        pol1= pol1.sig
    return paux

#FUNCION AÑADIDA
def existir_termino(polinomio,termino):
    aux= polinomio.termino_mayor
    while aux is not None and aux.info.termino > termino:
        aux= aux.sig
    if aux is not None and aux.info.termino == termino:
        return True
    else:
        return False

        


