from ejercicio5 import *

from ejercicio5 import *
def iniciar():
    alfabeto= [chr(i) for i in range(33,125)]
    Hash= TablaHash(len(alfabeto))
    mensaje= input('Ingrese el mensaje a encriptar: ')
    mensaje_encriptado= Hash.encriptar(mensaje)
    print('El mensaje encriptado es: ', mensaje_encriptado)
    mensaje_desencriptado= Hash.desencriptar(mensaje_encriptado)
    print('El mensaje desencriptado es: ', mensaje_desencriptado)

    


