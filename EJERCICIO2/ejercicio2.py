
matriz=[]

def crear_matriz(tamanio):
    matriz= [None]*tamanio
    return matriz

def definir_dimension_matriz():
    dimension= int(input('Ingrese la dimension de la matriz: '))
    return dimension

def crear_matriz_vacia(dimension):
    matriz= [None]*dimension
    for i in range(dimension):
        matriz[i]= [None]*dimension
    return matriz

def cargar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j]= int(input('Ingrese un numero: '))
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

def calcular_determinante_iterativo(matriz):
    print('El determinante de la matriz es: ', determinante_iterativo(matriz))

def calcular_determinante_recursivo(matriz):
    print('El determinante de la matriz es: ', determinante_recursivo(matriz))


def determinante_recursivo(matriz): #forma recursiva ya que se llama a si misma
    if len(matriz) == 1:
        return matriz[0][0]
    else:
        det = 0
        for i in range(len(matriz)):
            det += (-1)**i * matriz[0][i] * determinante_recursivo([fila[:i] + fila[i+1:] for fila in (matriz[1:])]) 
        return det


#forma iterativa

def determinante_iterativo(matriz): # es de forma iterativa ya que no se llama a si misma
    det = 0
    if len(matriz) == 1:
        return matriz[0][0]
    else:
        for i in range(len(matriz)):
            det += (-1)**i * matriz[0][i] * determinante_iterativo([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
    return det




