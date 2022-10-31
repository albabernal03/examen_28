from ejercicio2 import *

def iniciar():
    print("1. Determinante recursivo")
    print("2. Determinante iterativo")
    print("3. Salir")

    opcion= int(input("Ingrese una opcion: "))

    if opcion==1:
            dimension= definir_dimension_matriz()
            matriz= crear_matriz_vacia(dimension)
            matriz= cargar_matriz(matriz)
            mostrar_matriz(matriz)
            calcular_determinante_recursivo(matriz)

    elif opcion==2:
            dimension= definir_dimension_matriz()
            matriz= crear_matriz_vacia(dimension)
            matriz= cargar_matriz(matriz)
            mostrar_matriz(matriz)
            calcular_determinante_iterativo(matriz)

    elif opcion==3: 
            print("Hasta luego")
            exit()

    else:
            print("Opcion incorrecta")
        







