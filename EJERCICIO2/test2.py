import unittest

from ejercicio2 import *

class TestEjercicio2(unittest.TestCase):
    matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert determinante_recursivo(matriz1) == 0
    assert determinante_recursivo(matriz2) == 0
    assert determinante_recursivo(matriz3) == 0
    assert determinante_recursivo(matriz4) == 0

    assert determinante_iterativo(matriz1) == 0
    assert determinante_iterativo(matriz2) == 0
    assert determinante_iterativo(matriz3) == 0
    assert determinante_iterativo(matriz4) == 0
    

if __name__ == '__main__':
    unittest.main()

    