from ejercicio5 import *

def iniciar():
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        texto = input("Ingrese el texto a encriptar: ")
        encriptar(texto)
    elif opcion == 2:
        texto_encriptado = input("Ingrese el texto a desencriptar: ")
        desencriptar(texto_encriptado)
    elif opcion == 3:
        print("Hasta luego")
    else:
        print("Opcion incorrecta")


    