from ejercicio5 import *

def iniciar():
    print('1.Encriptar mensaje')
    print('2.Desencriptar mensaje')

    opcion= int(input('Ingrese una opcion: '))
    alfabeto= [(i) for i in range(33,125)]
    Hash= TablaHash(len(alfabeto))
    mensaje= input('Ingrese el mensaje: ')

    if opcion==1:
        mensaje_encriptado= Hash.encriptar(mensaje)
        print('Mensaje encriptado: ',mensaje_encriptado)

    elif opcion==2:
        mensaje_desencriptado= Hash.desencriptar(mensaje)
        print('Mensaje desencriptado: ',mensaje_desencriptado)

