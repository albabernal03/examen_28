from ejercicio2 import *

def main():

    print('1. Determinante iterativo')
    print('2. Determinante recursivo')

    opcion= int(input('Ingrese una opcion: '))
    
    dimension= definir_dimension_matriz()
    matriz= crear_matriz_vacia(dimension)
    matriz= cargar_matriz(matriz)
    mostrar_matriz(matriz)

    if opcion == 1:
        calcular_determinante_iterativo(matriz)
    elif opcion == 2:
        calcular_determinante_recursivo(matriz)


  
  







