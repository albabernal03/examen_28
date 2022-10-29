#forma recursiva
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


