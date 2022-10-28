import unittest

from ejercicio2 import *

class TestEjercicio2(unittest.TestCase):
    matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert determinante(matriz1) == 0
    assert determinante(matriz2) == 0
    assert determinante(matriz3) == 0
    assert determinante(matriz4) == 0
