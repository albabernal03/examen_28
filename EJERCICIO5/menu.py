from ejercicio5 import *

def iniciar():
    print('1.cifrar mensaje')
    print('2.descifrar mensaje')

    opcion= int(input('Ingrese una opcion: '))

    if opcion==1:
        mensaje= input('Ingrese el mensaje: ')
        print('Mensaje cifrado: ',cifrar(mensaje))

    elif opcion==2:
        mensaje= input('Ingrese el mensaje: ')
        print('Mensaje descifrado: ',descifrar(mensaje))



    