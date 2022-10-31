class TablaHash():
    def __init__(self, tam):
        '''Constructor de la clase TablaHash'''
        self.tam= tam
        self.tabla= [None]*self.tam

    def mostrar_tabla(self):
        '''Muestra la tabla'''
        for i in range(self.tam):
            print(i, self.tabla[i]) #a través de este print se puede ver como se va llenando la tabla

    def funcion_hash(self,caracter): #utilizamos el número mágico que en los apuntes se define como funcion de bernstein
        return ord(caracter)*33%self.tam

    def insertar(self,valor):
        '''Inserta un valor en la tabla'''
        pos= self.funcion_hash(valor)
        self.tabla[pos]= valor 

    def encriptar(self,mensaje):
        '''Encripta un mensaje'''
        mensaje_encriptado= ''
        for i in mensaje:
            self.insertar(i)
            mensaje_encriptado = mensaje_encriptado + chr(self.funcion_hash(i) + 33) #se le suma 33 para que el caracter sea imprimible
        return mensaje_encriptado

    def desencriptar(self,mensaje):
        '''Desencripta un mensaje'''
        mensaje_desencriptado= ''
        for i in mensaje:
            mensaje_desencriptado = mensaje_desencriptado + self.tabla[ord(i)-33]
        return mensaje_desencriptado

        


