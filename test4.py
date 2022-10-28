#hacemos el test del fichero ejercicio4.py

import unittest
from ejercicio4 import *

class TestEjercicio4(unittest.TestCase):
    def test_agregar_termino(self):
        p1= Polinomio()
        agregar_termino(p1,2,3)
        self.assertEqual(p1.termino_mayor.info.termino,2)
        self.assertEqual(p1.termino_mayor.info.valor,3)
        self.assertEqual(p1.termino_menor.info.termino,2)
        self.assertEqual(p1.termino_menor.info.valor,3)
        self.assertEqual(p1.grado,2)
        agregar_termino(p1,3,4)
        self.assertEqual(p1.termino_mayor.info.termino,3)
        self.assertEqual(p1.termino_mayor.info.valor,4)
        self.assertEqual(p1.termino_menor.info.termino,2)
        self.assertEqual(p1.termino_menor.info.valor,3)
        self.assertEqual(p1.grado,3)
        agregar_termino(p1,1,5)
        self.assertEqual(p1.termino_mayor.info.termino,3)
        self.assertEqual(p1.termino_mayor.info.valor,4)
        self.assertEqual(p1.termino_menor.info.termino,1)
        self.assertEqual(p1.termino_menor.info.valor,5)
        self.assertEqual(p1.grado,3)
        agregar_termino(p1,0,6)
        self.assertEqual(p1.termino_mayor.info.termino,3)
        self.assertEqual(p1.termino_mayor.info.valor,4)
        self.assertEqual(p1.termino_menor.info.termino,0)
        self.assertEqual(p1.termino_menor.info.valor,6)
        self.assertEqual(p1.grado,3)
        agregar_termino(p1,4,7)
        self.assertEqual(p1.termino_mayor.info.termino,4)
        self.assertEqual(p1.termino_mayor.info.valor,7)
        self.assertEqual(p1.termino_menor.info.termino,0)
        self.assertEqual(p1.termino_menor.info.valor,6)
        self.assertEqual(p1.grado,4)
        agregar_termino(p1,4,8)
        self.assertEqual(p1.termino_mayor.info.termino,4)
        self.assertEqual(p1.termino_maximo.info.valor,15)
        self.assertEqual(p1.termino_menor.info.termino,0)

        self.assertEqual(p1.grado,4)
        agregar_termino(p1,4,9)
        self.assertEqual(p1.termino_mayor.info.termino,4)



        self.assertEqual(p1.termino_menor.info.valor,6) 
        self.assertEqual(p1.grado,4)
        agregar_termino(p1,4,10)
        self.assertEqual(p1.termino_mayor.info.termino,4)
        self.assertEqual(p1.termino_mayor.info.valor,15)
        self.assertEqual(p1.termino_menor.info.termino,0)
        self.assertEqual(p1.termino_menor.info.valor,6)
        self.assertEqual(p1.grado,4)
        agregar_termino(p1,4,11)

        self.assertEqual(p1.termino_mayor.info.valor,15)
        self.assertEqual(p1.termino_menor.info.termino,0)









