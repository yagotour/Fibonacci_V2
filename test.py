#Tarea 1 Yago Touriño Medrano
#Archivo .py donde se llama a la clase "unittest"y se importa la función "fibonacci" del archivo fibo.py
#Se crea la clase TestFibonacci para verificar que la posición número "5" de la función es "3"

import unittest
from fibo import fibonacci
class TestFibonacci(unittest.TestCase):
    def test_posicion(self):
        result = fibonacci(5)
        self.assertEqual(result, 3, "Error, el resultado del test de la función \"fibonacci\" no es el esperado")