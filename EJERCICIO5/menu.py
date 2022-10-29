from ejercicio5 import *

def menu():
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        encriptar()
    elif opcion == 2:
        desencriptar()
    elif opcion == 3:
        print("Hasta luego")
    else:
        print("Opcion incorrecta")
        menu()

if __name__ == '__main__':
    menu()
    