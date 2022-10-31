from ejercicio5 import *

def iniciar():
    print('1.cifrar mensaje')
    print('2.descifrar mensaje')

    opcion= int(input('Ingrese una opcion: '))

    if opcion==1:
        mensaje= input('Ingrese el mensaje: ').upper()
        print('Mensaje cifrado: ',encriptar(mensaje))

    elif opcion==2:
        mensaje= input('Ingrese el mensaje: ').upper()
        print('Mensaje descifrado: ',desencriptar(mensaje))



    