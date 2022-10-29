#pasamos los test de ejercicio3.py

import unittest

from ejercicio3 import *

class TestEjercicio3(unittest.TestCase):
    
        def test_ordenar_naves_por_nombre_ascendente(self):
            lista = [Nave("Enterprise", 300, 5, 100),
                    Nave("Voyager", 200, 3, 50),
                    Nave("Defiant", 400, 7, 150),
                    Nave("Reliant", 500, 9, 200),
                    Nave("Intrepid", 100, 1, 10)]
            Nave.ordenar_naves_por_nombre_ascendente(lista)
            self.assertEqual(lista[0].nombre, "Defiant")
            self.assertEqual(lista[1].nombre, "Enterprise")
            self.assertEqual(lista[2].nombre, "Intrepid")
            self.assertEqual(lista[3].nombre, "Reliant")
            self.assertEqual(lista[4].nombre, "Voyager")
    
        def test_ordenar_naves_por_nombre_descendente(self):
            lista = [Nave("Enterprise", 300, 5, 100),
                    Nave("Voyager", 200, 3, 50),
                    Nave("Defiant", 400, 7, 150),
                    Nave("Reliant", 500, 9, 200),
                    Nave("Intrepid", 100, 1, 10)]
            Nave.ordenar_naves_por_nombre_descendente(lista)
            self.assertEqual(lista[0].nombre, "Voyager")
            self.assertEqual(lista[1].nombre, "Reliant")
            self.assertEqual(lista[2].nombre, "Intrepid")
            self.assertEqual(lista[3].nombre, "Enterprise")
            self.assertEqual(lista[4].nombre, "Defiant")
    
        def test_mostrar_nave(self):
            lista = [Nave("Enterprise", 300, 5, 100),
                    Nave("Voyager", 200, 3, 50),
                    Nave("Defiant", 400, 7, 150),
                    Nave("Reliant", 500, 9, 200),
                    Nave("Intrepid", 100, 1, 10)]
            self.assertEqual(mostrar_nave(lista), "Enterprise 300 5 100 Voyager 200 3 50 Defiant 400 7 150 Reliant 500 9 200 Intrepid 100 1 10")