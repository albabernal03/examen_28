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
        polinomio_termino_mayor= aux
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
    
def obtener

