class TablaHash():

    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [None] * tamanio

    def funcion_hash(self, clave):
        return clave % self.tamanio

    def encriptar(self, mensaje):
        mensaje_encriptado = ''
        for i in mensaje:
            mensaje_encriptado += chr(self.funcion_hash(ord(i)))
        return mensaje_encriptado

    def desencriptar(self, mensaje):
        mensaje_desencriptado = ''
        for i in mensaje:
            mensaje_desencriptado += chr(self.funcion_hash(ord(i)))
        return mensaje_desencriptado



#ejemplo de uso 

mensaje= 'Hola'

Hash= TablaHash(len(mensaje))

mensaje_encriptado= Hash.encriptar(mensaje)

mensaje_desencriptado= Hash.desencriptar(mensaje_encriptado)

print('Mensaje encriptado: ',mensaje_encriptado)

print('Mensaje desencriptado: ',mensaje_desencriptado)




