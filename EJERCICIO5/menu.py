from ejercicio5 import *

def iniciar():
    print('1.cifrar mensaje')
    print('2.descifrar mensaje')

    opcion= int(input('Ingrese una opcion: '))

    if opcion==1:
        mensaje= input('Ingrese el mensaje a encriptar: ')
        print('Mensaje encriptado: ',encriptar(mensaje))

iniciar()


    