#Este ejercicio lo vamos a resolver utilizqndo la estructura de pilas

class NodoPila(object): # objeto es un nodo de la pila
    info, sig = None, None # info: dato, sig: siguiente nodo

class Pila(object):
    def __init__(self,name):
        self.cima=None # cima: nodo superior de la pila
        self.tamanio= 0 # tamanio: cantidad de nodos en la pila
        self.name= name

def apilar(pila, dato):
    '''Agrega un nodo con el dato al tope de la pila'''
    nodo = NodoPila() # crea un nodo 
    nodo.info= dato # asigna el dato al nodo
    nodo.sig= pila.cima # el nodo apunta al nodo superior, si es que hay. El pila. lo pongo para que sea mas claro que es un atributo de la clase pila y no de la clase nodo
    pila.cima= nodo # el nodo pasa a ser el nodo superior
    pila.tamanio += 1 # incrementa el tamanio de la pila

def desapilar(pila):
    '''Elimina el nodo superior de la pila y devuelve su dato'''
    if not pila_vacia(pila):
        x= pila.cima.info # guarda el dato del nodo superior en x
        pila.cima= pila.cima.sig # el nodo superior pasa a ser el siguiente
        pila.tamanio -= 1 # decrementa el tamanio de la pila
        return x # devuelve el dato del nodo eliminado

def pila_vacia(pila):
    '''Devuelve True si la pila esta vacia'''
    return pila.cima is None

def en_cima(pila):
    '''Devuelve el dato del nodo superior de la pila'''
    if pila is not None:
        return pila.cima.info
    else:
        return None
    
def tamanio_pila(pila):
    '''Devuelve el tamanio de la pila'''
    return pila.tamanio

#RESOLVEMOS EL EJERCICO (HANOI):

pivote_incial= Pila("pivote_inicial")
pivote_auxiliar= Pila("pivote_auxiliar")
pivote_final= Pila("pivote_final")
n= int(input("Ingrese la cantidad de discos: "))

def hanoi(n, pivote_inicial,pivote_auxiliar,pivote_final):
    if n==1:
        apilar(pivote_final, desapilar(pivote_inicial))
        print('Mover disco de', pivote_inicial.name, 'a', pivote_final.name)
    else:
        hanoi(n-1,pivote_inicial, pivote_final, pivote_auxiliar)
        apilar(pivote_final, desapilar(pivote_inicial))
        print('Mover disco de', pivote_inicial.name, 'a', pivote_final.name)
        hanoi(n-1,pivote_auxiliar, pivote_inicial, pivote_final)

        
