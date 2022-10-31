class TablaHash():

    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [None] * tamanio

    def mostrar_tabla(self):
        return self.tabla

    def funcion_hash(self, caracter):
        return ord(caracter)*33 % self.tamanio #ord devuelve el codigo ascii del caracter y el 33 es el numero mágico, en los apuntes se definio como funcion de bernstein
        
    def agregar(self, elemento):
        hash= self.funcion_hash(elemento)
        if self.tabla[hash] == None:
            self.tabla[hash]= elemento
        else:
            print('La posicion esta ocupada')

    def encriptar(self,mensaje):
        mensaje_encriptado = ''
        for caracter in mensaje:
            self.agregar(caracter)
            resultado = resultado + str(self.funcion_hash(caracter) + 33)
        return resultado

    def desencriptar(self, mensaje):
        mensaje_desencriptado = ''
        for caracter in mensaje:
            mensaje_desencriptado = mensaje_desencriptado + str(self.mensaje_encriptado[ord(caracter)-33])

        return mensaje_desencriptado
