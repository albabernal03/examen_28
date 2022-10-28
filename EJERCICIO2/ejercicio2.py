#calcular determinante de una matriz 3*3 forma resursiva

#MATRIZ 3 X3 
def determinante(matriz): #forma recursiva
    if len(matriz) == 1:
        return matriz[0][0]
    else:
        det = 0
        for i in range(len(matriz)):
            det += (-1)**i * matriz[0][i] * determinante([fila[:i] + fila[i+1:] for fila in (matriz[1:])])
        return det


